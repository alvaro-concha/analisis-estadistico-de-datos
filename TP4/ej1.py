"""Ejercicio 1"""
import numpy as np


def ej1():
    x = (18.9, 17.4, 20.8, 18.3, 17.0)
    media_muestral = np.mean(x)
    mediana = np.median(x)
    varianza_muestral = np.var(x, ddof=1)
    varianza_muestral_sesgada = np.var(x, ddof=0)

    print(f"Media muestral\t{media_muestral:.2f}")
    print(f"Mediana\t\t{mediana:.2f}")
    print(f"Varianza muestral\t\t{varianza_muestral:.2f}")
    print(f"Varianza muestral sesgada\t{varianza_muestral_sesgada:.2f}")


if __name__ == "__main__":
    ej1()
