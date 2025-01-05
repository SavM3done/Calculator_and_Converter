# MainGUI settings -----
MAIN_DIMENSIONS = "321x267"

LEFT_BUTTON = {
    "text": "calculator",
    "background": "#00a8e8",
    "height": 10,
    "width": 10 
}

RIGHT_BUTTON = {
    "text": "converter",
    "background": "#00e89a",
    "height": 10,
    "width": 10
}

# CalculatorGUI settings -----
CALCULATOR_DIMENSIONS = "429x198"

ZERO = {
    "text": "0", 
    "fg": "black",
    "bg": "#e5edff"
}

ONE = {
    "text": "1", 
    "fg": "black",
    "bg": "#e5edff"
}

TWO = {
    "text": "2", 
    "fg": "black",
    "bg": "#e5edff"
}

THREE = {
    "text": "3", 
    "fg": "black",
    "bg": "#e5edff"
}

FOUR = {
    "text": "4", 
    "fg": "black",
    "bg": "#e5edff"
}

FIVE = {
    "text": "5", 
    "fg": "black",
    "bg": "#e5edff"
}

SIX = {
    "text": "6", 
    "fg": "black",
    "bg": "#e5edff"
}

SEVEN = {
    "text": "7", 
    "fg": "black",
    "bg": "#e5edff"
}

EIGHT = {
    "text": "8", 
    "fg": "black",
    "bg": "#e5edff"
}

NINE = {
    "text": "9", 
    "fg": "black",
    "bg": "#e5edff"
}

POINT = {
    "text": ".", 
    "fg": "black",
    "bg": "#e5edff"
}
ADDITION = { 
    "text": "+", 
    "fg": "black",
    "bg": "#318CE7"
}

SUBTRACTION = {
    "text": "\u2796",
    "fg": "black",
    "bg": "#318CE7"
}

MULTIPLICATION = { 
    "text": "\u2715",
    "fg": "black",
    "bg": "#318CE7"
}

DIVISION = {
    "text": "\u00F7",
    "fg": "black",
    "bg": "#318CE7"
}

EQUAL = {
    "text": " = ", 
    "fg": "black", 
    "bg": "#00a8e8"
}

SQUARE_ROOT = {
    "text": "\u221A", 
    "fg": "black",
    "bg": "#318CE7"
}
OPEN_PARENTHESIS = {
    "text": "(", 
    "fg": "black",
    "bg": "#318CE7"	
}

CLOSE_PARENTHESIS = {
    "text": ")", 
    "fg": "black", 
    "bg": "#318CE7"
}

# ConverterGUI settings -----
CONVERTER_DIMENSIONS = "550x179"
UNIT_TYPES = ["currency", "mass", "length"]

CONVERSION_BUTTON = {
    "text": "\u21BA",
    "bg": "#32CD32" 
}

CONVERSION_TYPES = {
    "width": 26, 
    "height": 10, 
    "values": UNIT_TYPES,
    "state": "readonly"
}

SELECTED_UNIT_CHECKBOX = {
    "width": 19, 
    "height": 3,
    "state": "readonly"
}

TARGET = {
    "width": 21,
    "state": "readonly"
}

TARGET_UNIT_CHECKBOX = {
    "width": 19, 
    "height": 3, 
    "state": "readonly"
}		

# Button in more GUIs -----

CLEAR = { 
    "text": "C", 
    "fg": "black", 
    "bg": "red"
}	