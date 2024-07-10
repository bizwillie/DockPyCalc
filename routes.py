# routes.py - Flask routes and UI handling

from flask import Blueprint, render_template, request, jsonify
from . import calculator, conversions, memory

# Define blueprint
calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/', methods=['GET', 'POST'])
def calculator_page():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = float(request.form['num1'])
        num2 = float(request.form.get('num2', 0))

        # Perform calculation based on operation
        if operation == 'add':
            result = calculator.add(num1, num2)
        elif operation == 'subtract':
            result = calculator.subtract(num1, num2)
        elif operation == 'multiply':
            result = calculator.multiply(num1, num2)
        elif operation == 'divide':
            result = calculator.divide(num1, num2)
        elif operation == 'modulus':
            result = calculator.modulus(num1, num2)
        elif operation == 'exponentiate':
            result = calculator.exponentiate(num1, num2)
        elif operation == 'square_root':
            result = calculator.square_root(num1)
        elif operation == 'logarithm':
            result = calculator.logarithm(num1, num2)
        elif operation == 'sine':
            result = calculator.sine(num1)
        elif operation == 'cosine':
            result = calculator.cosine(num1)
        elif operation == 'tangent':
            result = calculator.tangent(num1)
        else:
            result = "Invalid operation"

        # Store result in history (example)
        memory.add_history(result)

        return jsonify(result=result)

    return render_template('calculator.html')
