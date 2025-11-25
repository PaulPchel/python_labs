from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Прочитать текстовый файл и вернуть его содержимое как одну строку.

    Исключения:
        FileNotFoundError: если файл не найден.
        UnicodeDecodeError: если содержимое не может быть декодировано указанной кодировкой.
    """
    path = Path(path)
    with path.open("r", encoding=encoding) as f:
        return f.read()


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создать или перезаписать CSV-файл с разделителем запятая (,).

    Исключения:
        ValueError: если строки в `rows` имеют разную длину.
    """
    if not rows:
        with Path(path).open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(header)
        return

    expected_len = len(rows[0])
    if any(len(row) != expected_len for row in rows):
        raise ValueError("Все строки должны иметь одинаковую длину")

    path = Path(path)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)
