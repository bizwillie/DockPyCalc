from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

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

memory = []

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = request.form.get('num2')
            operation = request.form['operation']
            
            if operation == 'add':
                result = add(num1, float(num2))
            elif operation == 'subtract':
                result = subtract(num1, float(num2))
            elif operation == 'multiply':
                result = multiply(num1, float(num2))
            elif operation == 'divide':
                result = divide(num1, float(num2))
            elif operation == 'modulus':
                result = modulus(num1, float(num2))
            elif operation == 'exponentiate':
                result = exponentiate(num1, float(num2))
            elif operation == 'square_root':
                result = square_root(num1)
            elif operation == 'logarithm':
                result = logarithm(num1, float(num2) if num2 else 10)
            elif operation == 'sine':
                result = sine(num1)
            elif operation == 'cosine':
                result = cosine(num1)
            elif operation == 'tangent':
                result = tangent(num1)
            elif operation == 'memory_add':
                memory.append(num1)
                result = f"Added {num1} to memory."
            elif operation == 'memory_recall':
                if memory:
                    result = f"Memory: {memory[-1]}"
                else:
                    result = "Memory is empty."
            elif operation == 'memory_clear':
                memory.clear()
                result = "Memory cleared."
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Error: Invalid input"
        except Exception as e:
            result = f"Error: {str(e)}"

        return jsonify(result=result)
    return render_template('calculator.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
