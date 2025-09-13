
from typing import Protocol


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


class TemperatureConverter(Protocol):

    temperature: float

    def __init__(self, temperature: float) -> None: ...

    def convert(self) -> float: ...

class FahrenheitToCelciusConverter(TemperatureConverter):

    def __init__(self, temperature: float) -> None:
        self.temperature = temperature


    def convert(self) -> float:
        return (self.temperature - 32) * (5 / 9)


class CelciusToFahrenheitConverter(TemperatureConverter):

    def __init__(self, temperature: float) -> None:

        self.temperature = temperature

    def convert(self) -> float:
        return (self.temperature * (9 / 5)) + 32

class TemperatureConverterBuilder:

    def __init__(self, units_to: str, units_from: str, temperature: float) -> None:

        self.units_to = units_to
        self.units_from = units_from
        self.temperature = temperature

    def build(self) -> TemperatureConverter:

        if self.units_to == "Celcius" and self.units_from == "Fahrenheit":
            return FahrenheitToCelciusConverter(self.temperature)


        if self.units_to == "Fahrenheit" and self.units_from == "Celcius":
            return CelciusToFahrenheitConverter(self.temperature)


        raise NotImplementedError
