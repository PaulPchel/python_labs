from dataclasses import dataclass
from pathlib import Path
import csv
from typing import List


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> List[Student]:
        students = []
        with self.path.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != self.HEADER:
                raise ValueError("Некорректный заголовок CSV файла.")
            for row in reader:
                students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"])
                    )
                )
        return students

    def _write_all(self, students: List[Student]):
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.HEADER)
            for st in students:
                writer.writerow([st.fio, st.birthdate, st.group, st.gpa])

    def list(self) -> List[Student]:
        return self._read_all()

    def add(self, student: Student):
        with self.path.open("a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str) -> List[Student]:
        substr_lower = substr.lower()
        return [s for s in self.list() if substr_lower in s.fio.lower()]

    def remove(self, fio: str) -> int:
        students = self.list()
        filtered = [s for s in students if s.fio != fio]
        removed = len(students) - len(filtered)
        self._write_all(filtered)
        return removed

    def update(self, fio: str, **fields) -> int:
        students = self.list()
        updated_count = 0

        for st in students:
            if st.fio == fio:
                updated_count += 1
                for key, value in fields.items():
                    if hasattr(st, key):
                        if key == "gpa":
                            value = float(value)
                        setattr(st, key, value)

        if updated_count > 0:
            self._write_all(students)

        return updated_count

    def pretty_print(self, students: List[Student] = None):
        if students is None:
            students = self.list()
        if not students:
            print("Список студентов пуст.")
            return

        widths = [len(h) for h in self.HEADER]
        for s in students:
            widths[0] = max(widths[0], len(s.fio))
            widths[1] = max(widths[1], len(s.birthdate))
            widths[2] = max(widths[2], len(s.group))
            widths[3] = max(widths[3], len(f"{s.gpa:.2f}"))

        header_line = " | ".join(h.ljust(w) for h, w in zip(self.HEADER, widths))
        print(header_line)
        print("-" * len(header_line))

        for s in students:
            print(f"{s.fio.ljust(widths[0])} | {s.birthdate.ljust(widths[1])} | {s.group.ljust(widths[2])} | {s.gpa:.2f}")
