import json
from .models import Student
from pathlib import Path


def students_to_json(students: list[Student], path):
    path = Path(path)
    data = [s.to_dict() for s in students]
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def students_from_json(path) -> list[Student]:
    path = Path(path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Student.from_dict(x) for x in raw]
