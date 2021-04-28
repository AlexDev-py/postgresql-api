import os
from table import Students

db_host = os.environ.get("DB_HOST")  # URL к базе данных
students_table = Students(db_host)  # Инициализируем таблицу `Students`

# Создаем таблицу
print("Создание таблицы `Students`: ", students_table.create_table())
