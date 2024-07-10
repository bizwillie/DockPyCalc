from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import math
import matplotlib.pyplot as plt
import io
import base64

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

# Unit conversions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Memory and history
memory = []
history = []

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
            elif operation == 'celsius_to_fahrenheit':
                result = celsius_to_fahrenheit(num1)
            elif operation == 'fahrenheit_to_celsius':
                result = fahrenheit_to_celsius(num1)
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
            elif operation == 'history_clear':
                history.clear()
                result = "History cleared."
            elif operation == 'degrees_to_radians':
                result = math.radians(num1)
            elif operation == 'radians_to_degrees':
                result = math.degrees(num1)
            elif operation == 'absolute_value':
                result = abs(num1)
            elif operation == 'factorial':
                result = math.factorial(int(num1))
            else:
                result = "Invalid operation"
            
            if isinstance(result, (int, float)):
                history.append(result)
        except ValueError:
            result = "Error: Invalid input"
        except Exception as e:
            result = f"Error: {str(e)}"

        return jsonify(result=result)
    return render_template('calculator.html', history=history)

@app.route('/plot', methods=['POST'])
def plot():
    function = request.form['function']
    x_values = list(range(-10, 11))
    y_values = []

    for x in x_values:
        try:
            y = eval(function)
            y_values.append(y)
        except:
            y_values.append(None)
    
    plt.figure()
    plt.plot(x_values, y_values, marker='o')
    plt.title('Graph of {}'.format(function))
    plt.xlabel('x')
    plt.ylabel('y')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return jsonify(graph_url='data:image/png;base64,{}'.format(graph_url))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple authentication check
        if username == 'user' and password == 'pass':
            session['user'] = username
            return redirect(url_for('calculator'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
