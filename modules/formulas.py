from scipy import constants


# CURRENCY ----- last update: March 2024
CURRENCY_RATES = {
    "Euro": [1, 1.08, .86, 163.47, 1.66, 1.46, .97, 100], # Euro
    "USA Dollars": [0.93, 1, .79, 151.34, 1.53, 1.35, .9, 92.59], # USA Dollars
    "GB Pounds": [1.17, 1.26, 1, 191.09, 1.94, 1.71, 1.14, 116.9], # GB Pounds
    "Yen": [.0061, .0066, .0052, 1, .01, .0089, .006, .61], # Yen
    "Australian Dollars": [.6, .65, .52, 98.66, 1, .88, .59, 60.36], # Australian Dollars
    "Canadian Dollars": [.69, .74, 0.59, 112.03, 1.14, 1, .67, 68.53], # Canadian Dollars
    "Swiss Franc": [1.03, 1.11, .88, 167.77, 1.70, 1.50, 1, 102.63], # Swiss Franc
    "Russian Ruble": [.01, .011, .0086, 1.63, .021, .015, 0.0097, 1], # Russian Ruble
}


def get_currency_target(value, selected, target):
    target_index = list(CURRENCY_RATES.keys()).index(target)
    selected_rate = (CURRENCY_RATES[selected][target_index])
		
    return value * selected_rate

		
# MASS -----
MASS_CONVERSIONS = {
	  "Kilogram": 1, # Kilograms
    "Gram": constants.gram,
    "Metric ton": constants.metric_ton, 
    "Grain": constants.grain, 
    "Pound": constants.lb, 
    "Ounce": constants.oz, 
    "Stone": constants.stone, 
    "Long ton": constants.long_ton, 
    "Short ton": constants.short_ton, 
    "Troy ounce": constants.troy_ounce,
    "Troy pound": constants.troy_pound, 
    "Karat": constants.carat, 
    "Atomic mass unit": constants.atomic_mass
}


def get_mass_target(value, selected, target):
    result_in_kilograms = value * MASS_CONVERSIONS[selected] 
    return result_in_kilograms / MASS_CONVERSIONS[target]


# LENGTH -----
LENGTH_CONVERSIONS = {
	  "Inch": constants.inch,
    "Foot": constants.foot, 
    "Yard": constants.yard,
    "Mile": constants.mile,
    "Point": constants.pt,
    "Survey foot": constants.survey_foot, 
    "Survey mile": constants.survey_mile,
    "Nautical mile": constants.nautical_mile,
    "Fermi": constants.fermi, 
    "Ångström": constants.angstrom,
    "Micron": constants.micron, 
    "Astronomical unit": constants.au,
    "Light year": constants.light_year, 
    "Parsec":	constants.parsec, 
    "Metre":	1, # Metre
    "Kilogram":	constants.kilo  
}


def get_length_target(value, selected, target):
    result_in_meters = value * LENGTH_CONVERSIONS[selected] 
    return result_in_meters / LENGTH_CONVERSIONS[target]
