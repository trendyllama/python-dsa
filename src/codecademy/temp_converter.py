import logging
from typing import Protocol

logger = logging.getLogger(__name__)


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

    logger.debug("Converting %s degrees %s", temp, units)

    if units == "F" or units == "Fahrenheit":
        c = (temp - 32) * (5 / 9)
        logger.debug("Converted to %s degrees Celsius", c)
        return c
    elif units == "C" or units == "Celcius":
        f = (temp * (9 / 5)) + 32
        logger.debug("Converted to %s degrees Fahrenheit", f)
        return f
    else:
        msg = "Invalid units. Please use 'F' for Fahrenheit or 'C' for Celcius."
        logger.error(msg)
        raise ValueError(msg)


class TemperatureConverter(Protocol):
    temperature: float

    def __init__(self, temperature: float) -> None: ...

    def convert(self) -> float: ...


class FahrenheitToCelciusConverter(TemperatureConverter):
    def __init__(self, temperature: float) -> None:
        logger.debug(
            "Initializing FahrenheitToCelciusConverter with temperature: %s",
            temperature,
        )
        self.temperature = temperature

    def convert(self) -> float:
        return (self.temperature - 32) * (5 / 9)


class CelciusToFahrenheitConverter(TemperatureConverter):
    def __init__(self, temperature: float) -> None:
        logger.debug(
            "Initializing CelciusToFahrenheitConverter with temperature: %s",
            temperature,
        )

        self.temperature = temperature

    def convert(self) -> float:
        return (self.temperature * (9 / 5)) + 32


class TemperatureConverterBuilder:
    def __init__(self, units_to: str, units_from: str, temperature: float) -> None:
        self.units_to = units_to
        self.units_from = units_from
        self.temperature = temperature
        logger.debug(
            "Initializing TemperatureConverterBuilder with units_to: %s, units_from: %s, temperature: %s",
            units_to,
            units_from,
            temperature,
        )

    def build(self) -> TemperatureConverter:
        if self.units_to == "Celcius" and self.units_from == "Fahrenheit":
            return FahrenheitToCelciusConverter(self.temperature)

        if self.units_to == "Fahrenheit" and self.units_from == "Celcius":
            return CelciusToFahrenheitConverter(self.temperature)

        raise NotImplementedError
