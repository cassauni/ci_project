import pytest

from calculator import add, calculate, divide, modulo, multiply, power, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(7, 3) == 4


def test_multiply():
    assert multiply(4, 2.5) == 10


def test_divide():
    assert divide(9, 3) == 3


def test_power():
    assert power(2, 3) == 8


def test_modulo():
    assert modulo(10, 3) == 1


def test_zero_division_errors():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)


def test_calculate_dispatcher():
    assert calculate(2, 3, "+") == 5
    assert calculate(8, 2, "div") == 4


def test_calculate_unknown_operation():
    with pytest.raises(ValueError):
        calculate(1, 2, "sqrt")