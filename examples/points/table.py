from __future__ import annotations
from postgresql_api.Table import Table

# Инструмент для создания новых типов данных
# В этом же модуле присутствуют другие типы данных.
from postgresql_api.field_types import FieldType


"""
Представим, что нам необходимо хранить данные о точках на двумерной плоскости.
Мы не хотим делать отдельные поля `x` и `y` для хранения координат.
Поэтому мы реализуем новый тип данных `Position`
"""


class Position(FieldType):
    """
    Новый тип данных, который хранит координаты на двумерной плоскости
    `x` и `y`.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: tuple):
        """
        Будет вызван при вычитании.
        :return: self
        """

        self.x -= other[0]
        self.y -= other[1]
        return self

    def __add__(self, other: tuple):
        """
        Будет вызван при сложении.
        :return: self
        """

        self.x += other[0]
        self.y += other[1]
        return self

    def __repr__(self):
        """
        Будет вызван при переводе в строку.
        :return: (<self.x>;<self.y>)
        """

        return "(%f;%f)" % (self.x, self.y)

    # adapter и converter должны быть @classmethod

    @classmethod
    def adapter(cls, obj: Position) -> bytes:
        """
        Определяем метод `adapter`,
        который будет возвращать данные в том виде,
        в каком они будут храниться в таблице.
        :param obj: Объект данного класса.
        :return: bytes
        """

        return ("%f;%f" % (obj.x, obj.y)).encode()

    @classmethod
    def converter(cls, obj: bytes) -> Position:
        """
        Определяем метод `converter`,
        который будет возвращать объект этого класса,
        основываясь на данных, полученных из таблицы.
        :param obj: bytes
        :return: Объект данного класса.
        """

        return Position(*map(float, obj.decode("utf-8").split(";")))


class Points(Table):
    position: Position = Position(0, 0)
    color: str = "Blue"
    size: float = 1
