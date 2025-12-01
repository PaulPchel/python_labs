from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

students = students_from_json("data/lab08/students_input.json")
students_to_json(students, "data/lab08/students_output.json")

for s in students:
    print(s)


"""
python3 -m src.lab08.test
"""
