import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(3, 5) == -2
    assert Calculator.subtract(0, 0) == 0

def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 3) == -6
    assert Calculator.multiply(0, 5) == 0

def test_divide():
    assert Calculator.divide(6, 3) == 2
    assert Calculator.divide(5, 2) == 2.5
    assert Calculator.divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Calculator.divide(5, 0)

def test_power():
    assert Calculator.power(2, 3) == 8
    assert Calculator.power(5, 0) == 1
    assert Calculator.power(4, 0.5) == 2

def test_sqrt():
    assert Calculator.sqrt(9) == 3
    assert Calculator.sqrt(0) == 0
    assert Calculator.sqrt(2) == pytest.approx(1.41421356237)

def test_sqrt_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        Calculator.sqrt(-1)

def test_evaluate():
    assert Calculator.evaluate("2 + 3") == 5
    assert Calculator.evaluate("10 - 4") == 6
    assert Calculator.evaluate("3 * 4") == 12
    assert Calculator.evaluate("10 / 2") == 5
    assert Calculator.evaluate("2 ** 3") == 8
    assert Calculator.evaluate("(2 + 3) * 4") == 20

def test_evaluate_invalid():
    with pytest.raises(ValueError):
        Calculator.evaluate("2 +")
    with pytest.raises(ValueError):
        Calculator.evaluate("abc")