# conversions.py - Unit conversions module

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Length conversions
def meters_to_feet(m):
    return m * 3.28084

def kilometers_to_miles(km):
    return km * 0.621371

# Weight conversions
def kilograms_to_pounds(kg):
    return kg * 2.20462

def grams_to_ounces(g):
    return g * 0.035274

# Volume conversions
def liters_to_gallons(l):
    return l * 0.264172

def milliliters_to_ounces(ml):
    return ml * 0.033814
