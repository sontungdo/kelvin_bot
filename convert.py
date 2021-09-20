
def convert(amount, unit):
    """
    Function to convert a measurement between Celsius and Fahrenheit
    @param amount: the measurement number
    @param unit: unit of measure (either F or C)
    @return: measurement number in the other unit
    """
    unit = unit.upper()
    if (unit == "F"):
        return (amount - 32) / 1.8
    elif (unit == "C"):
        return amount * 1.8 + 32
    else:
        return 0

def to_kelvin(amount, unit):
    """
    Function to convert a temperature measurement to Kelvin
    @param amount: the measurement number
    @param unit: unit of measure (either F or C)
    @return: measurement number in the other unit
    """
    unit = unit.upper()
    if (unit == "F"):
        return (amount - 32) / 1.8 + 273.15
    elif (unit == "C"):
        return amount + 273.15
    else:
        return 0
