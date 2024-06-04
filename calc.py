import tkinter as tk
from tkinter import messagebox


class BasicCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Calculator")

        # Initialize instance attributes
        self.entry1 = None
        self.entry2 = None
        self.result_var = None

        # Initialize the user interface
        self.create_widgets()

    def create_widgets(self):
        # Create and place the input fields
        tk.Label(self.master, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
        self.entry1 = tk.Entry(self.master)
        self.entry1.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.master, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
        self.entry2 = tk.Entry(self.master)
        self.entry2.grid(row=1, column=1, padx=10, pady=5)

        # Create and place the operation buttons
        tk.Button(self.master, text="Add", command=lambda: self.perform_operation('add')).grid(row=2, column=0, padx=10,
                                                                                               pady=5)
        tk.Button(self.master, text="Subtract", command=lambda: self.perform_operation('subtract')).grid(row=2,
                                                                                                         column=1,
                                                                                                         padx=10,
                                                                                                         pady=5)

        tk.Button(self.master, text="Multiply", command=lambda: self.perform_operation('multiply')).grid(row=3,
                                                                                                         column=0,
                                                                                                         padx=10,
                                                                                                         pady=5)

        tk.Button(self.master, text="Divide", command=lambda: self.perform_operation('divide')).grid(row=3, column=1,
                                                                                                     padx=10, pady=5)

        # Create and place the result display
        self.result_var = tk.StringVar()
        tk.Label(self.master, text="Result:").grid(row=4, column=0, padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.result_var, state='readonly').grid(row=4, column=1, padx=10, pady=5)

    def perform_operation(self, operation):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            result = None  # Initialize the result variable
            if operation == 'add':
                result = self.add(num1, num2)
            elif operation == 'subtract':
                result = self.subtract(num1, num2)
            elif operation == 'multiply':
                result = self.multiply(num1, num2)
            elif operation == 'divide':
                result = self.divide(num1, num2)
            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers")

