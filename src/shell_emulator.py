import os
import socket
import sys


def get_prompt():
    """Формирует приглашение вида username@hostname:cwd$."""
    user = os.getenv("USER", "user")
    host = socket.gethostname()
    cwd = os.getcwd()
    home = os.path.expanduser("~")
    if cwd.startswith(home):
        cwd = cwd.replace(home, "~", 1)
    return f"{user}@{host}:{cwd}$ "


def parse_input(user_input):
    """Простой парсер: разделяет строку по пробелам."""
    return user_input.split()


def cmd_ls(args):
    """Заглушка для команды ls."""
    print(f"Вызвана команда ls с аргументами: {args}")


def cmd_cd(args):
    """Заглушка для команды cd."""
    print(f"Вызвана команда cd с аргументами: {args}")


def main():
    """Основной цикл REPL."""
    while True:
        try:
            user_input = input(get_prompt())
        except (KeyboardInterrupt, EOFError):
            print("\nВыход...")
            break

        if not user_input.strip():
            continue

        parts = parse_input(user_input)
        command = parts[0]
        args = parts[1:]

        if command == "exit":
            print("Завершение работы эмулятора.")
            break
        elif command == "ls":
            cmd_ls(args)
        elif command == "cd":
            cmd_cd(args)
        else:
            print(f"Ошибка: неизвестная команда '{command}'")


if __name__ == "__main__":
    main()