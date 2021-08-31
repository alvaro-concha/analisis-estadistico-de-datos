"""Ejercicio 7: El número de la suerte"""
import numpy as np
import pandas as pd
from scipy.stats import binom
import plotly.graph_objects as go

np.random.seed(42)


class LanzarDados:
    """Simulacion de un lanzamiento de dados."""

    def __init__(self, n_dados=5, n_target=3):
        self.n_dados = n_dados
        self.n_target = n_target

    def __call__(self):
        dice_toss = np.random.choice(range(1, 7), size=self.n_dados)
        return {
            "k": (dice_toss == self.n_target).sum(),
        }


def distribucion_binomial(n=5, p=1 / 6):
    """Distribucion exacta (binomial), del problema de lanzamiento de dados."""
    k = np.arange(n + 1)
    return k, binom(n=n, p=p).pmf(k)


def ej7():
    """Ejercicio 7."""
    n_ensemble = 1000
    resultados = []
    for _ in range(n_ensemble):
        juego = LanzarDados()
        resultados.append(juego())
    resultados = pd.DataFrame(resultados)
    k, dist = distribucion_binomial()
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(x=resultados["k"], histnorm="probability", name="Simulación")
    )
    fig.add_trace(go.Scatter(x=k, y=dist, name="Binomial"))
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text="El número de la suerte",
        xaxis_title_text="Eventos",
        yaxis_title_text="Probabilidad",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej7()
