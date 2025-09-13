from typing import Protocol, runtime_checkable

import numpy as np
from scipy.stats import norm


@runtime_checkable
class BlackScholesCalculator(Protocol):
    underlying_price: float
    strike_price: float
    years_to_maturity: int | float
    risk_free_rate: float
    sigma: int | float
    option_price: np.float64 | None

    def calculate_option_price(self) -> np.float64: ...


class CallOptionCalculator(BlackScholesCalculator):
    def __init__(
        self,
        underlying_price: float,
        strike_price: float,
        years_to_maturity: int | float,
        risk_free_rate: float,
        sigma: int | float,
    ) -> None:
        self.underlying_price = underlying_price
        self.strike_price = strike_price
        self.years_to_maturity = years_to_maturity
        self.risk_free_rate = risk_free_rate
        self.sigma = sigma
        self.option_price = None

    def calculate_option_price(self) -> np.float64:
        d1 = (
            np.log(self.underlying_price / self.strike_price)
            + (self.risk_free_rate + self.sigma**2 / 2) * self.years_to_maturity
        ) / (self.sigma * np.sqrt(self.years_to_maturity))
        d2 = d1 - self.sigma * np.sqrt(self.years_to_maturity)

        self.option_price = self.underlying_price * norm.cdf(
            d1
        ) - self.strike_price * np.exp(
            -self.risk_free_rate * self.years_to_maturity
        ) * norm.cdf(d2)

        if self.option_price is None:
            raise ValueError

        return self.option_price


class PutOptionCalculator(BlackScholesCalculator):
    def __init__(
        self,
        underlying_price: float,
        strike_price: float,
        years_to_maturity: int | float,
        risk_free_rate: float,
        sigma: int | float,
    ) -> None:
        self.underlying_price = underlying_price
        self.strike_price = strike_price
        self.years_to_maturity = years_to_maturity
        self.risk_free_rate = risk_free_rate
        self.sigma = sigma
        self.option_price = None

    def calculate_option_price(self) -> np.float64:
        d1 = (
            np.log(self.underlying_price / self.strike_price)
            + (self.risk_free_rate + self.sigma**2 / 2) * self.years_to_maturity
        ) / (self.sigma * np.sqrt(self.years_to_maturity))
        d2 = d1 - self.sigma * np.sqrt(self.years_to_maturity)

        self.option_price = self.strike_price * np.exp(
            -self.risk_free_rate * self.years_to_maturity
        ) * norm.cdf(-d2) - self.underlying_price * norm.cdf(-d1)

        if self.option_price is None:
            raise ValueError

        return self.option_price


class BlackScholesCalculatorBuilder:
    def __init__(
        self,
        underlying_price: float,
        strike_price: float,
        years_to_maturity: int | float,
        risk_free_rate: float,
        sigma: int | float,
    ) -> None:
        self.underlying_price = underlying_price
        self.strike_price = strike_price
        self.years_to_maturity = years_to_maturity
        self.risk_free_rate = risk_free_rate
        self.sigma = sigma

    def build(self, option_type: str) -> BlackScholesCalculator:
        if option_type == "c":
            return CallOptionCalculator(
                self.underlying_price,
                self.strike_price,
                self.years_to_maturity,
                self.risk_free_rate,
                self.sigma,
            )
        else:
            return PutOptionCalculator(
                self.underlying_price,
                self.strike_price,
                self.years_to_maturity,
                self.risk_free_rate,
                self.sigma,
            )


def black_scholes(
    underlying_price: float,
    strike_price: float,
    years_to_expiration: int | float,
    r: float,
    sigma: int | float,
    input_type: str = "c",
) -> np.float64:
    """
    Calculates the price of a European-style option using the Black-Scholes model.

    Args:
      S: The current stock price.
      K: The strike price of the option.
      T: The time to maturity of the option, in years.
      r: The risk-free interest rate.
      sigma: The volatility of the stock price.
      type: The type of option, either "c" for call or "p" for put.

    Returns:
      The price of the option.

    Example:
    >>> black_scholes(100, 100, 1, 0.05, 0.2, "c")
    np.float64(10.450583572185565)
    >>> black_scholes(100, 100, 1, 0.05, 0.2, "p")
    np.float64(5.573526022256971)
    """

    builder = BlackScholesCalculatorBuilder(
        underlying_price, strike_price, years_to_expiration, r, sigma
    )
    calculator = builder.build(input_type)

    return calculator.calculate_option_price()
