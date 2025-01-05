from tkinter import *
import tkinter as tk
import math
import modules.settings as settings


class CalculatorGUI:
    def __init__(self, root):
			  # Window options
        self.configure = root.configure(bg="grey")
        self.title = root.title("Calculator")
        self.geometry = root.geometry(settings.CALCULATOR_DIMENSIONS)
        self.resizable = root.resizable(0, 0)
		
        # Handle the calculations and show the result in the Entry field
        self.expression = "" 
        
        # Content in the Entry field
        self.equation = StringVar() 
        
        # Entry field with its position in the grid
        self.display = Entry(root, textvariable=self.equation)
        self.display.grid(columnspan=4, ipadx=100)
        

        # First row in the GUI. Contains "(", ")", "square root" and "C" buttons
        self.open_parenthesis = Button(
            root, 
            **settings.OPEN_PARENTHESIS, 
            command=lambda: self.append_to_display("(")
        )
        self.open_parenthesis.grid(row=3, column=0, sticky=["WE"])

        self.close_parenthesis = Button(
            root,	
            **settings.CLOSE_PARENTHESIS, 
            command=lambda: self.append_to_display(")")
        )
        self.close_parenthesis.grid(row=3, column=1, sticky=["WE"])

        self.square_root = Button(
            root, 
            **settings.SQUARE_ROOT, 
            command=self.calculate_square_root
        )
        self.square_root.grid(row=3, column=2, sticky=["WE"]) 
        
        self.clear = Button(
            root, 
            **settings.CLEAR, 
            command=self.clear_display
        )
        self.clear.grid(row=3, column=3, sticky=["WE"])
        

        # Second row in the GUI. Contains "7", "8" "9" and "/" buttons.
        self.seven = Button(
            root, 
            **settings.SEVEN, 
            command=lambda: self.append_to_display(7)
        )
        self.seven.grid(row=4, column=0, sticky=["WE"]) 
        
        self.eight = Button(
            root, 
            **settings.EIGHT, 
            command=lambda: self.append_to_display(8)
        )
        self.eight.grid(row=4, column=1, sticky=["WE"]) 
        
        self.nine = Button(
            root, 
            **settings.NINE, 
            command=lambda: self.append_to_display(9)
        )
        self.nine.grid(row=4, column=2, sticky=["WE"]) 
             
        self.division = Button(
            root, 
            **settings.DIVISION, 
            command=lambda: self.append_to_display("/")
        )
        self.division.grid(row=4, column=3, sticky=["WE"]) 
        

        # Third row in the GUI. Contains "4", "5", "6", and "x"
        self.four = Button(
            root, 
            **settings.FOUR, 
            command=lambda: self.append_to_display(4)
        )
        self.four.grid(row=5, column=0, sticky=["WE"]) 
           
        self.five = Button(
            root, 
            **settings.FIVE, 
            command=lambda: self.append_to_display(5)
        )
        self.five.grid(row=5, column=1, sticky=["WE"])
        
        self.six = Button(
            root, 
            **settings.SIX, 
            command=lambda: self.append_to_display(6)
        )
        self.six.grid(row=5, column=2, sticky=["WE"]) 
        
        self.multiplication = Button(
            root, 
            **settings.MULTIPLICATION, 
            command=lambda: self.append_to_display("*")
        )
        self.multiplication.grid(row=5, column=3, sticky=["WE"]) 

        # Fourth row in the GUI. Contains "1", "2", "3", and "-" buttons
        self.one = Button(
            root, 
            **settings.ONE, 
            command=lambda: self.append_to_display(1)
        )
        self.one.grid(row=6, column=0, sticky=["WE"]) 

        self.two = Button(
            root, 
            **settings.TWO, 
            command=lambda: self.append_to_display(2)
        )
        self.two.grid(row=6, column=1, sticky=["WE"])   
             
        self.three = Button(
            root, 
            **settings.THREE, 
            command=lambda: self.append_to_display(3)
        )
        self.three.grid(row=6, column=2, sticky=["WE"]) 
            
        self.subtraction = Button(
            root, 
            **settings.SUBTRACTION, 
            command=lambda: self.append_to_display("-")
        )
        self.subtraction.grid(row=6, column=3, sticky=["WE"]) 
        
        # Fifth row in the GUI. Contains ".", "0", "=" and "+" buttons
        self.point = Button(
            root, 
            **settings.POINT, 
            command=lambda: self.append_to_display(".")
        )
        self.point.grid(row=7, column=0, sticky=["WE"])

        self.zero = Button(
            root, 
            **settings.ZERO, 
            command=lambda: self.append_to_display(0)
        )
        self.zero.grid(row=7, column=1, sticky=["WE"]) 
        
        self.equal = Button(
            root, 
            **settings.EQUAL, 
            command=self.calculate_result
        )
        self.equal.grid(row=7, column=2, sticky=["WE"])
        
        self.addition = Button(
            root, 
            **settings.ADDITION, 
            command=lambda: self.append_to_display("+")
        )
        self.addition.grid(row=7, column=3, sticky=["WE"])	 

    # Functions -----
    
    # Add the button selected in the display
    def append_to_display(self, num): 
        self.equation.set(self.expression)
        self.expression += str(num) 
        

    def calculate_result(self):   
      try:	
        total = str(eval(self.expression))
        self.equation.set(total)
        self.expression = str(total)

      except: 
        self.handle_error


    def clear_display(self): 
        self.equation.set("") 
        self.expression = "" 


    def calculate_square_root(self):
      try:
        conversion = float(self.equation.get())
        self.equation.set(math.sqrt(conversion))
        self.expression = str(math.sqrt(conversion))

      except: 
        self.handle_error()


    def handle_error(self):
        self.equation.set(" ERROR ")
        self.expression = ""


left_root = Tk() 
CalculatorGUI(left_root)