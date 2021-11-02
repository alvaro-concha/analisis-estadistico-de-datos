"""Ejercicio 4"""
import numpy as np


def ej4():
    """Ejercicio 4."""
    q = 1.64
    x = np.array([13.4, 8.52, 12.7, 9.9, 12.8])
    n = len(x)
    x_bar = x.mean()
    s = x.std(ddof=1)
    print(f"Media muestral: {x_bar:.1f}")
    print(f"Desviación estándar muestral: {s:.1f}")
    print(
        f"Intervalo de Student 90% para la media: {x_bar:.1f} +- {q*s/np.sqrt(n):.1f}"
    )


if __name__ == "__main__":
    ej4()
