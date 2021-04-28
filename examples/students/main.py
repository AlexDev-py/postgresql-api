"""

Сначала запустите скрипты `create_table.py` и `insert_data.py`.

"""

import os
from table import Students

students = Students(os.environ.get("DB_HOST"))

print("\n      Просмотрим все данные в таблице Students")
# `return_list=True` - вернет список, даже если найден всего один объект
for obj in students.filter(return_list=True):
    print(obj, "\n")

print(
    "      Как видим у всех объектов есть свой `id`."
    "\n      Он создаётся автоматически и никогда не повторяется."
)
print(
    "\n      При фильтрации можно указывать действие(=, !=, >, <, >=, <=),\n"
    "      сделать это можно вот так:\n"
    "      age_no=14, данное выражение будет означать age != 14\n"
    "      так же и с другими действиями\n"
    "      no - !=, gt - >, lt - <, egt - >=, elt - <=\n"
    "      ! Поле и действие должны отделяться подчеркиванием !"
)

print("\n      Получим студентов младше 22 лет")
for obj in students.filter(return_list=True, age_lt=22):
    print(obj, "\n")

print(
    "      Допустим у Макса(id=3) было день рождение,\n"
    "      нам нужно изменить его возраст в базе данных.\n"
    "      Для этого нам нужно получить его данные:"
)
obj = students.filter(first_name="Max", last_name="Brown")
print(obj)

print(
    "\n      Просмотрим возраст Макса,\n"
    "      для этого воспользуемся объектом класса который получили ранее:"
)
print(f"{obj.age=}")

print("\n      Изменим его возраст")
obj.age += 1
print(f"{obj.age=}")

print("\n      Сохраним изменения, используя метод `save`")
print(f"{obj.save()=}")

print(
    "\n      Сделаем то же самое с остальными учениками."
    "\n      Но в этот раз будем использовать метод `update`.\n"
)

for obj in students.filter(first_name_no="Max", last_name_no="Brown"):
    print(f"{obj.id=}", f"{obj.update(age=obj.age + 1)=}")

print("\n      Попробуем получить список всех учеников с именем Bob:")

# `return_type=visual` вернёт массив данных объекта
# `return_type=classes` вернёт массив объектов класса
print(students.filter(return_type="visual", first_name="Bob"))

print(
    "\n      Как мы видим это не список, а просто объект.\n"
    "      Что бы получить список нужно указать параметр `return_list=True`"
)

print(students.filter(return_type="visual", return_list=True, first_name="Bob"))

print("\n      Посмотрим на таблицу в целом")
for obj in students.filter(return_list=True, return_type="visual"):
    print(obj)

print("\n      Попробуем изменить оценки одного из учеников.")
obj = students.filter(id=3)
print(f"{obj.id=} {obj.marks=}")
obj.marks.insert(0, 4)
obj.marks.remove(3)
obj.marks.extend([5, 5])
print(f"{obj.marks=}")
print(f"{obj.save()=}")

print("\n      Получим ученика используя return_type=visual")
obj = students.filter(id=2, return_type="visual")
print(obj)
print(
    "      Получим объект класса на основе этих данных, используя students.get_class():"
)
obj = students.get_class(obj)
print(obj)
print(
    "      Мы получили точно такой же класс, как если бы использовали return_type=classes"
)
