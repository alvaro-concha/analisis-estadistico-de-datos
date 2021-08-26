"""Ejercicio 9

Simular dos variables aleatorias $X_1$ y $X_2$ que siguen distribuciones de Poisson con parámetros $\mu_1 = 1$ y $\mu_2 = 2$ respectivamente.

Calcular la variable $Y = X_1 + X_2$.

Repetir la simulación 1000 veces.

Graficar la distribución de la variable $Y$ y comparar con una distribución de probabilidad adecuada.
"""
import numpy as np
import pandas as pd
from scipy.stats import poisson
import plotly.graph_objects as go

np.random.seed(42)


class SumarPoisson:
    """Simulacion de suma de variables aleatorias con distribucion de Poisson."""

    def __init__(self, mu1=1, mu2=2):
        self.mu1 = mu1
        self.mu2 = mu2

    def __call__(self):
        x1, x2 = np.random.poisson(lam=(self.mu1, self.mu2))
        return {
            "y": x1 + x2,
            "x1": x1,
            "x2": x2,
        }


def distribucion_poisson(mu, k_max=20):
    """Distribucion de Poisson."""
    k = np.arange(k_max + 1)
    return k, poisson(mu=mu).pmf(k)


def ej9():
    """Ejercicio 9."""
    n_ensemble = 1000
    resultados = []
    for _ in range(n_ensemble):
        juego = SumarPoisson()
        resultados.append(juego())
    resultados = pd.DataFrame(resultados)
    fig = go.Figure()
    fig.add_trace(
        go.Histogram(x=resultados["y"], histnorm="probability", name="Simulación")
    )
    for mu in [1, 2, 3]:
        k, dist = distribucion_poisson(mu=mu)
        fig.add_trace(go.Scatter(x=k, y=dist, name=f"Poiss(mu={mu})"))
    fig.update_traces(opacity=0.75)
    fig.update_xaxes(range=[0, 15])
    fig.update_layout(
        title_text="Suma de variables aleatorias de Poisson",
        xaxis_title_text="Ocurrencias",
        yaxis_title_text="Probabilidad",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej9()
