#!/usr/bin/env python3
"""
Simple Number Addition GUI Application
A form with two input fields and a sum output field.
"""

import tkinter as tk
from tkinter import messagebox

class AddNumbersApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Addition Calculator")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create the GUI widgets."""
        
        # Title Frame
        title_frame = tk.Frame(self.root, bg="#2c3e50")
        title_frame.pack(fill=tk.X, pady=0)
        
        title_label = tk.Label(
            title_frame,
            text="Number Addition Calculator",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )
        title_label.pack()
        
        # Main Frame
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Number 1
        number1_label = tk.Label(
            main_frame,
            text="Number 1:",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        number1_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.number1_entry = tk.Entry(
            main_frame,
            font=("Arial", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        self.number1_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Number 2
        number2_label = tk.Label(
            main_frame,
            text="Number 2:",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        number2_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.number2_entry = tk.Entry(
            main_frame,
            font=("Arial", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE
        )
        self.number2_entry.pack(fill=tk.X, pady=(0, 20))
        
        # Add Button
        add_btn = tk.Button(
            main_frame,
            text="Add",
            command=self.calculate_sum,
            bg="#3498db",
            fg="white",
            font=("Arial", 11, "bold"),
            padx=30,
            pady=10,
            relief=tk.RAISED,
            cursor="hand2"
        )
        add_btn.pack(pady=(0, 20))
        
        # Sum Result
        sum_label = tk.Label(
            main_frame,
            text="Sum:",
            font=("Arial", 11, "bold"),
            bg="#f0f0f0"
        )
        sum_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.sum_display = tk.Entry(
            main_frame,
            font=("Arial", 12),
            width=30,
            bd=2,
            relief=tk.GROOVE,
            state="readonly",
            justify=tk.CENTER
        )
        self.sum_display.pack(fill=tk.X)
        
        # Focus on first entry field
        self.number1_entry.focus()
    
    def calculate_sum(self):
        """Calculate the sum of the two numbers."""
        try:
            num1_str = self.number1_entry.get().strip()
            num2_str = self.number2_entry.get().strip()
            
            if not num1_str or not num2_str:
                messagebox.showwarning("Input Error", "Please enter both numbers!")
                return
            
            num1 = float(num1_str)
            num2 = float(num2_str)
            
            total = num1 + num2
            
            # Update sum display
            self.sum_display.config(state="normal")
            self.sum_display.delete(0, tk.END)
            self.sum_display.insert(0, str(total))
            self.sum_display.config(state="readonly")
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers!")

def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = AddNumbersApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
