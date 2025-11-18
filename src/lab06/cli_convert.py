import argparse
from pathlib import Path
import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def run_json2csv(input_file: str, output_file: str):
    try:
        json_to_csv(input_file, output_file)
        print(f"JSON -> CSV успешно: {output_file}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def run_csv2json(input_file: str, output_file: str):
    try:
        csv_to_json(input_file, output_file)
        print(f"CSV -> JSON успешно: {output_file}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def run_csv2xlsx(input_file: str, output_file: str):
    try:
        csv_to_xlsx(input_file, output_file)
        print(f"CSV -> XLSX успешно: {output_file}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных CSV/JSON/XLSX")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV")

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON")

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX")

    args = parser.parse_args()

    if args.command == "json2csv":
        run_json2csv(args.input, args.output)
    elif args.command == "csv2json":
        run_csv2json(args.input, args.output)
    elif args.command == "csv2xlsx":
        run_csv2xlsx(args.input, args.output)

if __name__ == "__main__":
    main()


