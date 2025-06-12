import numpy as np
from scipy.stats import norm


def black_scholes(S, K, T, r, sigma, type="c"):
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
    """

    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if type == "c":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


price = float(input("Whats the current price of the underlying?: "))
strike = float(input("What's the strike price of the option?: "))
time_to_mat = float(
    input("What's the time to maturity of the option? (input in terms of years): ")
)
risk_free_rate = float(input("What's the risk free rate? (%1 as 1.00): "))
implied_vol = float(input("What's the implied vol of the underlying? (%1 as 1.00): "))
type = str(input("Is it a call or a put? (c or p): "))

print(
    "Black Scholes theo = {}".format(
        black_scholes(price, strike, time_to_mat, risk_free_rate, implied_vol, type)
    )
)