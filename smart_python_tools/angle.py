#!/usr/local/bin/python3
# coding:utf-8

"""
@author: joey
@file: angle.py
@time: 2020/07/20
@describe:度分秒制角度计算
"""

import abc
from math import modf


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}'
        cls.__counter += 1

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner):  # self:<__main__.Unit object at 0x7febf31431d0>
        print("__get__")
        return getattr(instance, self.storage_name) if instance else self


class Validated(abc.ABC, AutoStorage):
    @abc.abstractmethod
    def validate(self, instance, value):
        """Return validated values or raise ValueError"""
        pass

    def __set__(self, instance, value):
        self.validate(instance, value)
        super().__set__(instance, value)


class Unit(Validated):
    """A unit whose number is >= 0"""

    def validate(self, instance, value):
        if value < 0:
            raise ValueError('value must be >= 0')
        return value


class EnterMeta(type):
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storge_name = f'_{type_name}#{key}'
                cls._field_names.append(key)


class Entity(metaclass=EnterMeta):  # type()创建函数
    @classmethod
    def field_names(cls):
        yield from (name for name in cls._field_names)


class Angle(Entity):
    # 验证输入为正
    degree = Unit()
    minute = Unit()
    second = Unit()

    # # 测试
    # a = Angle()
    # a.degree = 1
    # a.degree

    def __init__(self, degree, minute, second):
        self.degree = float(degree)
        self.minute = float(minute)
        self.second = float(second)

    def __str__(self):
        return fr'{type(self).__name__}({self.degree}°,{self.minute}°,{self.second}°)'

    __repr__ = __str__

    def to_degree(self):
        return Angle(self.degree + self.minute / 60.0 + self.second / 3600.0, 0.0, 0.0)

    def to_second(self):
        return Angle(0.0, self.degree * 60.0 + self.minute + self.second / 60.0, 0.0)

    def to_dms(self):
        d_frac, d_int = modf(self.degree)
        m_frac, m_int = modf(d_frac * 60.0)
        s_int = round(m_frac * 60.0)
        return Angle(d_int, m_int, s_int)

    def __add__(self, other):
        d = self.degree + other.degree
        m = self.minute + other.minute
        s = self.second + other.second
        if s > 60.0:
            s -= 60.0
            m += 1.0
        if m > 60.0:
            m -= 60.0
            d += 1.0
        return Angle(d, m, s)

    def __sub__(self, other):   # 减法不够减，借位
        if other.second > self.second:
            self.second += 60
            self.minute -= 1.0
        if other.minute > self.minute:
            self.minute += 60
            self.degree -= 1.0

        d = self.degree - other.degree
        m = self.minute - other.minute
        s = self.second - other.second
        return Angle(d, m, s)

    def __mul__(self, scalar: float):
        d = self.degree * scalar
        m = self.minute * scalar
        s = self.second * scalar
        if s > 60.0:
            s -= 60.0
            m += 1.0
        if m > 60.0:
            m -= 60.0
            d += 1.0
        return Angle(d, m, s)

    def __truediv__(self, scalar: float):
        d, remainder = divmod(self.degree, scalar)
        self.minute += remainder * 60
        m, remainder = divmod(self.minute, scalar)
        self.second += remainder * 60
        s = self.second / scalar
        return Angle(d, m, s)


a = Angle(30, 20, 10)
b = Angle(60, 50, 40)
print(a / 1.0)

