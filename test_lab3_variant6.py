import unittest

from lab3_variant6 import (
    Counter,
    NumberHelper,
    PriceCalculator,
    SaleDiscount,
    Student,
    StudentDiscount,
)


class Lab3Tests(unittest.TestCase):
    def test_static_method(self):
        self.assertTrue(NumberHelper.is_even(10))
        self.assertFalse(NumberHelper.is_even(7))

    def test_counter(self):
        counter = Counter()
        counter.increase()
        counter.increase()
        counter.decrease()
        self.assertEqual(counter.value, 1)

    def test_student(self):
        student = Student("Анна", "221141", 4.5)
        self.assertEqual(student.name, "Анна")
        self.assertEqual(student.group, "221141")

    def test_price_strategy(self):
        self.assertEqual(PriceCalculator(StudentDiscount()).calculate(1000), 900)
        self.assertEqual(PriceCalculator(SaleDiscount()).calculate(1000), 800)


if __name__ == "__main__":
    unittest.main()

