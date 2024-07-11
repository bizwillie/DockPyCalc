# routes.py - Flask routes and UI handling

from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session, flash
from . import calculator, conversions, memory, auth
import matplotlib.pyplot as plt
import io
import base64
import math

# Define blueprint
calc_bp = Blueprint('calc', __name__)

@calc_bp.route('/', methods=['GET', 'POST'])
def calculator_page():
    if 'username' not in session:
        return redirect(url_for('calc.login'))

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

@calc_bp.route('/plot', methods=['POST'])
def plot_graph():
    function = request.form['function']

    # Generate plot data
    try:
        x = range(-10, 11)
        y = eval(function, {'__builtins__': None}, {'x': x, 'math': math})
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph of ' + function)
        plt.grid(True)

        # Convert plot to base64 string for HTML img tag
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return jsonify(success=True, graph_data=image_base64)

    except Exception as e:
        print(str(e))
        return jsonify(success=False, error=str(e))

@calc_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if auth.authenticate(username, password):
            session['username'] = username
            return redirect(url_for('calc.calculator_page'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@calc_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('calc.login'))

@calc_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            auth.create_user(username, password)
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('calc.login'))
        except Exception as e:
            flash(str(e), 'danger')
    return render_template('register.html')
