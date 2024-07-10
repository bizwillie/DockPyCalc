# Advanced Calculator Application

Welcome to the Advanced Calculator application, a comprehensive tool for performing basic arithmetic operations, advanced scientific calculations, unit conversions, and dynamic plotting of mathematical functions.

## Features

### Basic Arithmetic Operations

- **Addition**: Add two numbers together.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another, handling zero division gracefully.

### Advanced Scientific Functions

- **Exponentiation**: Compute the power of a number.
- **Modulus**: Calculate the remainder of a division.
- **Square Root**: Compute the square root of a number.
- **Logarithm**: Compute logarithms with customizable bases.
- **Trigonometric Functions**: Calculate sine, cosine, and tangent in both degrees and radians.

### Unit Conversions

- **Celsius to Fahrenheit**: Convert temperatures from Celsius to Fahrenheit.
- **Fahrenheit to Celsius**: Convert temperatures from Fahrenheit to Celsius.

### Memory Management

- **History**: Keep track of previous calculation results.
- **Memory Functions**: Add results to memory, recall the last result, and clear memory history.

### Interactive Plotting

- **Graph Plotting**: Plot user-defined mathematical functions dynamically.
- **Plot Types**: Support for plotting various functions including polynomials, trigonometric functions, and more.

## Architecture

The application is structured with a modular architecture for scalability and maintainability:

- **calculator.py**: Handles basic arithmetic and scientific operations.
- **conversions.py**: Manages unit conversion functionalities.
- **memory.py**: Provides memory management capabilities.
- **auth.py**: Implements user authentication and session management.
- **routes.py**: Defines Flask routes for UI handling and integration of backend functionalities.

## Technologies Used

- **Python**: Core language for backend calculations and logic.
- **Flask**: Web framework for building web applications.
- **JavaScript (jQuery, Plotly.js)**: Enhances frontend interactivity and dynamic plotting capabilities.
- **HTML/CSS (Bootstrap)**: Stylesheets and UI components for a responsive and visually appealing user interface.
- **Docker**: Containerization for seamless deployment across different environments.

## Getting Started

To run the application locally:

1. Clone this repository.
2. Install dependencies listed in `requirements.txt`.
3. Build and run the Docker container using `docker build -t advanced-calculator .` and `docker run -p 5000:5000 advanced-calculator`.

## Contributors

- Matt Wilson
- ChatGPT

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
