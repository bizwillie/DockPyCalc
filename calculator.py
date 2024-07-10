# calculator.py - Basic arithmetic and scientific operations module

import math

# Basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

# Scientific operations
def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Cannot take square root of a negative number"

def logarithm(x, base=10):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error: Logarithm of non-positive number is undefined"

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))