import os

from table import Points, Position

points = Points(os.environ.get("DB_HOST"))  # Инициализируем таблицу `Points`

print(points.insert(position=Position(x=1.2, y=6.9), size=2))

# Создаст объект, полностью опираясь на значения `по умолчанию`
print(points.insert())

print(points.insert(position=Position(1, 1.1)))
