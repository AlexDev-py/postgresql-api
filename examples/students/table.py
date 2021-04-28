from postgresql_api.Table import Table


class Students(Table):
    # Поле `first_name`. Тип данных: `str`. Значение по умолчанию: отсутствует
    first_name: str
    last_name: str
    age: int
    # Поле `course`. Тип данных: `int`. Значение по умолчанию: `1`
    course: int = 1
    salary: int = 5000
    marks: list = []
