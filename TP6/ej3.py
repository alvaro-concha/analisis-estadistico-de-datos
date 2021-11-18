"""Ejercicio 3"""
import numpy as np
from scipy.stats import norm, chisquare, chi2
from scipy.integrate import romberg
import matplotlib.pyplot as plt
import seaborn as sns


def my_chisquare(f_obs, f_exp):
    """Calcula el chi-cuadrado de una distribución normal."""
    chisq = np.sum((f_obs - f_exp) ** 2 / f_exp)
    p = 1.0 - chi2.cdf(chisq, len(f_obs))
    return chisq, p


def ej3():
    """Ejercicio 3."""
    x = np.loadtxt("chi2.dat")
    num_cuts = 20
    num_discarded = 2
    percentile_cuts = np.linspace(0, 100, num_cuts)
    if num_discarded == 0:
        observed, bins = np.histogram(x, bins=np.percentile(x, percentile_cuts))
    else:
        observed, bins = np.histogram(
            x, bins=np.percentile(x, percentile_cuts[num_discarded:-num_discarded])
        )
    domain = 0.5 * (bins[1:] + bins[:-1])
    dx = bins[1:] - bins[:-1]
    n = len(x)
    expected = np.vectorize(romberg)(norm.pdf, bins[:-1], bins[1:]) * n

    chisq, p = chisquare(f_obs=observed, f_exp=expected)
    print(f"scipy: statistic {chisq:.2f}, p-value {p * 100.0:.1e}%")

    chisq, p = my_chisquare(f_obs=observed, f_exp=expected)
    print(f"nuestra: statistic {chisq:.2f}, p-value {p * 100.0:.1e}%")

    if num_discarded == 0:
        plot_widths = dx - (domain[-1] - domain[0]) * 0.2 / (num_cuts)
    else:
        plot_widths = dx - (domain[-1] - domain[0]) * 0.2 / (
            num_cuts - 2 * num_discarded
        )

    plt.figure(figsize=(18, 8))
    sns.set_context("paper", font_scale=1.5)
    plt.bar(domain, observed / dx, width=plot_widths, alpha=0.5, label="Observado")
    plt.plot(domain, expected / dx, label="Esperado")
    plt.title("Test Chi-Cuadrado para Histogramas")
    plt.xlabel(r"$x$")
    plt.ylabel(r"Densidad")
    plt.legend()
    plt.show()
    plt.close()

    plt.figure(figsize=(18, 8))
    sns.set_context("paper", font_scale=1.5)
    plt.bar(domain, observed, width=plot_widths, alpha=0.5, label="Observado")
    plt.plot(domain, expected, label="Esperado")
    plt.title("Test Chi-Cuadrado para Histogramas")
    plt.xlabel(r"$x$")
    plt.ylabel(r"Frecuencia")
    plt.legend()
    plt.show()
    plt.close()


if __name__ == "__main__":
    ej3()
