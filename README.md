# Basic Calculator

A simple graphical user interface (GUI) based calculator implemented using Python's `tkinter` library. This calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Error handling for invalid inputs and division by zero

## Requirements

- Python 3.x
- `tkinter` library (comes pre-installed with Python)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/barishizm/Calculator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd calculator
    ```

## Usage

1. Run the `calc.py` script:
    ```bash
    python calc.py
    ```
2. A window will appear with input fields and buttons for each arithmetic operation.
3. Enter two numbers in the input fields.
4. Click on the desired operation button to perform the calculation.
5. The result will be displayed in the result field.

## Code Overview

The main functionality is encapsulated in the `Calculator` class within `calc.py`:

- **`__init__(self, master)`**: Initializes the calculator and creates the GUI elements.
- **`create_widgets(self)`**: Sets up the input fields, buttons, and result display.
- **`perform_operation(self, operation)`**: Performs the selected arithmetic operation and handles errors.
- **Static methods (`add`, `subtract`, `multiply`, `divide`)**: Define the basic arithmetic operations.
