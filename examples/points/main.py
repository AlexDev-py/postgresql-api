"""

Сначала запустите скрипты `create_table.py` и `insert_data.py`.

"""

import os
from typing import List

from table import Points, Position

points = Points(os.environ.get("DB_HOST"))

print("\n      Получим все точки, которые находятся не на нулевых координатах")
objects: List[Points] = points.filter(return_list=True, position_no=Position(0, 0))

for obj in objects:
    print(obj, "\n")

print("\n      Увеличим их размер")
for obj in objects:
    print(f"{obj.id=}", f"{obj.update(size=obj.size + 1)=}")

print("\n      Получим точки, размер которых не превышает 2, и сделаем их зелёными")
for obj in points.filter(return_list=True, size_elt=2):
    print(f"{obj.id=}", f'{obj.update(color="green")=}')

print("\n      Изменим позицию первой точки")
obj = points.filter(id=1)
print(f"{obj.position=}")
obj.position += (0.8, 3.1)
print(f"{obj.position=}")
print(f"{obj.save()=}")

print("\n      Изменим позицию второй точки")
obj = points.filter(id=2)
print(f"{obj.position=}")
obj.position = Position(2, 10)
print(f"{obj.position=}")
print(f"{obj.save()=}")

print("\n      Посмотрим на таблицу в целом")
for obj in points.filter(return_list=True):
    print(obj, "\n")
