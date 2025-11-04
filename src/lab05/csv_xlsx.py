import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if not csv_file.suffix.lower() == ".csv":
        raise ValueError("Неверный тип файла, ожидается .csv")

    # Создаём XLSX только если его нет
    if not xlsx_file.exists():
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        with csv_file.open(encoding="utf-8") as f:
            for row in csv.reader(f):
                ws.append(row)

        # автоширина колонок
        for column_cells in ws.columns:
            length = max(len(str(cell.value)) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = max(length, 8)

        wb.save(xlsx_file)

