"""Ejercicio 1"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def probabilidad(k, n_coca, n_total, n_elegidos):
    """Calcula la probabilidad de sacar k cocas de una bolsa de n_total en n_elegidos."""
    return (
        100.0
        * np.math.comb(n_coca, k)
        * np.math.comb(n_total - n_coca, n_elegidos - k)
        / np.math.comb(n_total, n_elegidos)
    )


def ej1():
    """Ejercicio 1."""
    n_coca = 4
    n_total = 9
    n_elegidos = 4
    k = np.arange(n_elegidos + 1)
    p = np.vectorize(probabilidad)(k, n_coca, n_total, n_elegidos)

    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    plt.bar(k, p)
    for i in range(n_elegidos + 1):
        exponente = int(-np.log10(p[i])) + 1
        text = f"{p[i]:.0e}" if (exponente > 3) else f"{p[i]:.{exponente + 1}f}"
        plt.text(k[i], p[i], text, ha="center", va="bottom")
    plt.title("Test Coca-Pepsi")
    plt.xlabel(r"Número de aciertos $k$")
    plt.ylabel(r"Probabilidad por azar $P(k)$ ó p-value (%)")
    plt.show()
    plt.close()


if __name__ == "__main__":
    ej1()
