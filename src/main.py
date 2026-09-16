"""CLI-интерфейс менеджера задач."""
import argparse
import sys


def add_task(title: str) -> None:
    """Добавляет задачу (заглушка)."""
    print(f"[OK] Задача добавлена: {title}")


def list_tasks() -> None:
    """Показывает список задач (заглушка)."""
    print("[INFO] Список задач пуст.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Добавить задачу")
    add_parser.add_argument("title", type=str, help="Название задачи")

    subparsers.add_parser("list", help="Показать задачи")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    return 0


if __name__ == "__main__":
    sys.exit(main())