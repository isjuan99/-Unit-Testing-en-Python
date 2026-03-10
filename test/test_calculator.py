import unittest
from src.calculator import suma, subtraccion, divide, multiply

class calculatorTestCase(unittest.TestCase):
    def test_suma(self):
        assert suma(2, 3) == 5
        assert suma(-1, 1) == 0
        assert suma(0, 0) == 0

    def test_subtraccion(self):
        assert subtraccion(5, 2) == 3
        assert subtraccion(1, -1) ==2
        assert subtraccion(0, 0) == 0

    def test_divide(self):
        assert divide(10, 2) == 5


    def test_multiply(self):
        assert multiply(3, 4) == 12

