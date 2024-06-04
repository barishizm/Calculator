import tkinter as tk
from tkinter import messagebox


class BasicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")

        # Initialize the user interface
        self.create_widgets()
