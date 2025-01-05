from tkinter import * 
import modules.settings as settings


# GUI on start. Let the user chose between the calculator and the converter
class MainGUI():
    def __init__(self, master):
        # Window options
        self.master = master
        self.geometry = settings.MAIN_DIMENSIONS
        self.title = master.title("Custom Calculator")
        self.resizable = master.resizable(0, 0)
        
        self.frame = Frame(master)
        self.frame.pack()
        
        # Add a custom message for the user
        self.label = Label(
          self.frame,
          text="Choose your calculation mode please"
        )
        self.label.pack(side=TOP)
        
        # Onclick destroy the window and open the calculator
        self.calculator = Button(
          self.frame, 
          **settings.LEFT_BUTTON,
          command= lambda: self.run_calculator()
        )
        self.calculator.pack(fill=BOTH, expand=True, side=LEFT)
        
        # Onclick destroy the window and open the converter
        self.converter = Button(
          self.frame, 
          **settings.RIGHT_BUTTON,
          command= lambda: self.run_converter()
        )
        self.converter.pack(fill=BOTH, expand=True, side=RIGHT)


    # Functions -----

    def run_calculator(self):
      root.destroy()
      import modules.calculator
      
    def run_converter(self):
      root.destroy()
      import modules.converter


if "__main__" == __name__:
	root = Tk()
	MainGUI(root)
	mainloop()