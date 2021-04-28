import os

from table import Points

db_host = os.environ.get("DB_HOST")  # URL к базе данных
points_table = Points(db_host)  # Инициализируем таблицу `Points`

# Создаем таблицу
print("Создание таблицы `Points`: ", points_table.create_table())
