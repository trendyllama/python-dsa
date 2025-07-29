import numpy as np
from scipy.stats import norm


def black_scholes(
    S: float, K: float, T: int | float, r: float, sigma: int | float, input_type: str = "c"
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

    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if input_type == "c":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
