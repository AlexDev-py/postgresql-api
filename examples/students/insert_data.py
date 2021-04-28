import os
from table import Students

students = Students(os.environ.get("DB_HOST"))

print(
    students.insert(
        first_name="Bob",
        last_name="Gray",
        age=20,
        # аргументы `по умолчанию` можно не указывать
        # course=1,
        # salary=5000,
        # изменяем значение по умолчанию
        marks=[5, 5, 4, 5],
    )
)

print(
    students.insert(
        first_name="Max",
        last_name="Brown",
        age=23,
        course=3,
        salary=10000,
        marks=[5, 5, 5, 5],
    )
)

print(
    students.insert(
        first_name="Joni", last_name="White", age=20, marks=[5, 3, 4, 5], salary=3500
    )
)
