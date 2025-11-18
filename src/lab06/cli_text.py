import argparse
from pathlib import Path
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

def cmd_cat(file_path: str, number_lines: bool):
    path = Path(file_path)
    if not path.exists():
        print(f"Ошибка: файл не найден: {file_path}", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if number_lines:
                print(f"{i}: {line.rstrip()}")
            else:
                print(line.rstrip())

def cmd_stats(file_path: str, top_count: int):
    path = Path(file_path)
    if not path.exists():
        print(f"Ошибка: файл не найден: {file_path}", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        text = f.read()

    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top_count}:")
    for word, count in top_n(freq, top_count):
        print(f"{word}: {count}")

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    sub = parser.add_subparsers(dest="command", required=True)

    cat_parser = sub.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = sub.add_parser("stats", help="Частота слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()

    if args.command == "cat":
        cmd_cat(args.input, args.n)
    elif args.command == "stats":
        cmd_stats(args.input, args.top)

if __name__ == "__main__":
    main()



