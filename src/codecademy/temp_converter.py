def conversion(units: str, temp: float):
    """
    Converts temperature between Fahrenheit and Celcius.
    Example:
    >>> conversion("F", 32)
    0.0
    >>> conversion("C", 0)
    32.0
    >>> conversion("F", 100)
    37.77777777777778
    >>> conversion("C", 100)
    212.0
    """
    if units == "F" or units == "Fahrenheit":
        c = (temp - 32) * (5 / 9)
        return c
    elif units == "C" or units == "Celcius":
        f = (temp * (9 / 5)) + 32
        return f
    else:
        raise ValueError(
            "Invalid units. Please use 'F' for Fahrenheit or 'C' for Celcius."
        )
