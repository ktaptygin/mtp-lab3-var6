"""Лабораторная работа № 3. Вариант 6."""

from dataclasses import dataclass
from typing import Callable


class NumberHelper:
    @staticmethod
    def is_even(number: int) -> bool:
        """Проверяет, является ли число чётным."""
        return number % 2 == 0


class Counter:
    def __init__(self, value: int = 0):
        self.value = value

    def increase(self) -> None:
        self.value += 1

    def decrease(self) -> None:
        self.value -= 1

    def __str__(self) -> str:
        return str(self.value)


@dataclass
class Student:
    name: str
    group: str
    average_mark: float

    def show_info(self) -> None:
        print(f"Студент: {self.name}")
        print(f"Группа: {self.group}")
        print(f"Средний балл: {self.average_mark}")


class RegularPrice:
    def calculate(self, price: float) -> float:
        return price


class StudentDiscount:
    def calculate(self, price: float) -> float:
        return price * 0.9


class SaleDiscount:
    def calculate(self, price: float) -> float:
        return price * 0.8


class PriceCalculator:
    def __init__(self, strategy: Callable[[float], float]):
        self.strategy = strategy

    def calculate(self, price: float) -> float:
        return self.strategy.calculate(price)


def run_demo() -> None:
    print("Задание 6. Статический метод")
    print(NumberHelper.is_even(12))

    print("\nЗадание 8. Класс-счётчик")
    counter = Counter(5)
    counter.increase()
    counter.decrease()
    print(f"Значение счётчика: {counter}")

    print("\nЗадание 2. Класс Студент")
    student = Student("Константин Таптыгин", "221141", 4.6)
    student.show_info()

    print("\nЗадание 4. Strategy для расчёта цены")
    price = 1000
    for name, strategy in (
        ("Обычная цена", RegularPrice()),
        ("Скидка студента", StudentDiscount()),
        ("Распродажа", SaleDiscount()),
    ):
        calculator = PriceCalculator(strategy)
        print(f"{name}: {calculator.calculate(price):.2f} руб.")


if __name__ == "__main__":
    run_demo()

