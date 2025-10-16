import sys
import argparse
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n
from lab04.io_txt_csv import read_text, write_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчёта по частоте слов в тексте.")
    parser.add_argument(
        "--in", dest="input_path", default="data/lab04/input.txt",
        help="путь к входному файлу (по умолчанию: data/lab04/input.txt)"
    )
    parser.add_argument(
        "--out", dest="output_path", default="data/lab04/report.csv",
        help="путь к выходному CSV (по умолчанию: data/lab04/report.csv)"
    )
    args = parser.parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    text = read_text(input_path)
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    rows = [(word, count) for word, count in sorted_items]

    write_csv(rows, output_path, header=("word", "count"))

    total_words = len(tokens)
    unique_words = len(freq)
    top5 = top_n(freq, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

"""
Для запуска:
python3 src/lab04/text_report.py --in /Users/paulpchelintsev/Desktop/python_labs/data/lab04/input.txt
"""
