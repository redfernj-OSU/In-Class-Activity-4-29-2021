import calc
import pytest

def test_add():
    assert calc.add(2,2) == 4

def test_subtract():
    assert calc.subtract(2,2) == 0

def test_multiply():
    assert calc.multiply(2,2) == 4

def test_divide():
    assert calc.divide(2,2) == 1

def test_fail():
    assert calc.divide(2,0) == 0