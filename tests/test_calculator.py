# tests/test_calculator.py

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add the parent directory to Python's path

from calculator import add, subtract, multiply, divide, modulus, exponentiate, square_root, logarithm, sine, cosine, tangent

# Basic arithmetic tests
def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == "Error: Cannot divide by zero"
    assert divide(-10, 2) == -5

# Scientific operation tests
def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(7, 2) == 1
    with pytest.raises(ZeroDivisionError):
        modulus(4, 0)

def test_exponentiate():
    assert exponentiate(2, 3) == 8
    assert exponentiate(10, 0) == 1
    assert exponentiate(0, 5) == 0

def test_square_root():
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(-1) == "Error: Cannot take square root of a negative number"

def test_logarithm():
    assert logarithm(100) == pytest.approx(2, rel=1e-3)
    assert logarithm(10, 2) == pytest.approx(3.32193, rel=1e-3)
    assert logarithm(0) == "Error: Logarithm of non-positive number is undefined"

def test_trigonometric_functions():
    assert sine(0) == pytest.approx(0, rel=1e-3)
    assert cosine(0) == pytest.approx(1, rel=1e-3)
    assert tangent(45) == pytest.approx(1, rel=1e-3)

# Additional tests can be added for memory functions once implemented in calculator.py
