"""Ejercicio 2"""
import numpy as np
from scipy.stats import norm


def ej2():
    """Ejercicio 2."""
    mu = 100
    sigma = 30
    bar_x = 50.8
    n = 10
    z = (bar_x - mu) / (sigma / np.sqrt(n))
    pvalue = norm.cdf(z) * 100.0
    print(f"Z-Test: statistic {z:.2f}, p-value {pvalue:.0e}%")

    alpha = 0.05
    z_c = norm.ppf(alpha)
    print(f"\tvalor crítico {z_c:.2f}, alpha {alpha * 100.0:.1f}%")


if __name__ == "__main__":
    ej2()
