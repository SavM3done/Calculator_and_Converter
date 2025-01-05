from tkinter import *
from tkinter.ttk import Combobox
import modules.settings as settings
import modules.formulas as formulas


class ConverterGUI:
    def __init__(self, root):
        # Window options
        self.configure = root.configure(bg="#00e89a")
        self.title = root.title("converter")
        self.geometry = root.geometry(settings.CONVERTER_DIMENSIONS) 
        self.resizable = root.resizable(0, 0)
        self.columns = root.columnconfigure(0, weight=1)
        self.rows = root.rowconfigure(1, weight=1)
        
        # Handle the calculations and show the result in the Entry field
        self.expression = ''

        # Top frame. Contains the buttons and the Combobox with the unit -----
        self.top_frame = Frame(root, bg="#00e89a")
        self.top_frame.grid(row=0, column=0, sticky=W+E)

        # Show the result in the right display
        self.conversion_button = Button(
          self.top_frame, 
          **settings.CONVERSION_BUTTON,
          command= lambda: self.get_values_for_formulas()
        )
        self.conversion_button.grid(row=0, column=0, padx=30, pady=10)
        
        # Main combobox. Default option is "Currency"
        self.actual_unit_type = StringVar(value=settings.UNIT_TYPES[0])
        self.unit_types_combobox = Combobox(
          self.top_frame, 
          **settings.CONVERSION_TYPES,
          textvariable=self.actual_unit_type, 
        )
        self.unit_types_combobox.bind("<<ComboboxSelected>>", self.get_selected_constants)   
        self.unit_types_combobox.grid(row=0, column=1, padx=(20), pady=10)

        # Clear both displays
        self.clear = Button(
          self.top_frame, 
          **settings.CLEAR,
          command=self.clear_displays
        )
        self.clear.grid(row=0, column=3, padx=(20, 10))  


        # Bottom frame -----
        self.bottom_frame = Frame(root, bg="#00e89a")
        self.bottom_frame.grid(row=1, column=0, sticky=W+E)

        # Input field
        self.selected_value = StringVar()
        self.selected_display = Entry(
          self.bottom_frame, 
          width=21, 
          textvariable=self.selected_value
        )
        self.selected_display.grid(row=1, column=0, padx=(30, 0), pady=(20, 0), sticky=S)
        
        
        # Select the input unit
        self.selected_unit = StringVar()
        self.selected_unit_checkbox = Combobox (
          self.bottom_frame, 
          **settings.SELECTED_UNIT_CHECKBOX,
          textvariable=self.selected_unit
        ) 
        self.selected_unit_checkbox.grid(row=2, column=0, padx=(30, 0), sticky=E+W+N) 
        self.selected_unit_checkbox["values"] = list(formulas.CURRENCY_RATES.keys())
        
        
        # Output field. It's not allowed to write
        self.target_value = StringVar()
        self.target_display = Entry(
            self.bottom_frame,
            **settings.TARGET,
            textvariable=self.target_value 
        )
        self.target_display.grid(row=1, column=1, padx=(0, 15), pady=(20, 0), sticky=S) 

        # Select the output unit
        self.target_unit = StringVar()
        self.target_unit_checkbox = Combobox (
          self.bottom_frame, 
          **settings.TARGET_UNIT_CHECKBOX,
          textvariable=self.target_unit
        )
        self.target_unit_checkbox.grid(row=2, column=1, padx=(0, 15), sticky=E+W+N)
        self.target_unit_checkbox["values"] = list(formulas.CURRENCY_RATES.keys())


    # When select an option in the main Combobox, change the fields in the sub-Combobox
    def get_selected_constants(self, event):
        if self.unit_types_combobox.get() == settings.UNIT_TYPES[0]:
            selected = list(formulas.CURRENCY_RATES.keys())
          
        elif self.unit_types_combobox.get() == settings.UNIT_TYPES[1]:
            selected = list(formulas.MASS_CONVERSIONS.keys())
          
        else: 
            selected = list(formulas.LENGTH_CONVERSIONS.keys())

        self.selected_unit_checkbox["values"] = selected
        self.target_unit_checkbox["values"] = selected


    def clear_displays(self): 
        self.expression = ""
        self.selected_value.set("")
        self.target_value.set("")

    # Catch the text and the bottom checkboxes as formula and handle the error 
    def get_values_for_formulas(self):
        
        try:
            self.calculate_result(
                float(self.selected_value.get()),
                str(self.selected_unit.get()), 
                str(self.target_unit.get())
            )

        except:
            print(float(self.selected_value.get()),
                str(self.selected_unit), 
                str(self.target_unit))
            self.target_value.set(" ERROR ")

    # Call the formulas.py function based on the main Combobox value
    def calculate_result(self, value, selected, target):
        
        if self.actual_unit_type.get() == settings.UNIT_TYPES[0]:
            result = formulas.get_currency_target(value, selected, target)
        
        elif self.actual_unit_type.get() == settings.UNIT_TYPES[1]:
            result = formulas.get_mass_target(value, selected, target)
        
        else:
            result = formulas.get_length_target(value, selected, target)
        
        self.target_value.set(result)


left_gui = Tk()
ConverterGUI(left_gui)