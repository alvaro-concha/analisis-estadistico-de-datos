"""Ejercicio 1"""
import numpy as np


def ej1():
    """Ejercicio 1."""
    sigma = 5.9
    q = 1.64
    x = np.array([67.6, 57.4, 63.0, 68.0, 63.1])
    n = len(x)
    x_bar = x.mean()
    print(f"Intervalo CL 90% para la media: {x_bar:.1f} +- {q*sigma/np.sqrt(n):.1f}")


if __name__ == "__main__":
    ej1()
