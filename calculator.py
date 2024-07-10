from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

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

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Error: Cannot take square root of a negative number"

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
