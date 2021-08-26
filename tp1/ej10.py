"""Ejercicio 10 (Para entregar)

Simular una variable aleatoria Y que sigue una distribución de Poisson con parámetro $\mu = 10$.

Suponer que el resultado de la simulación es $Y = k$.

A continuación simular $k$ variables de Bernoulli $X_i$ con $i = 1, \dots, k$ con parámetro $p = 0.7$.

Calcular el valor de una nueva variable Z definida como $Z = \sum_{i=1}^k X_i$.

Repetir la simulación 1000 veces, construir un histograma de frecuencia de $Z$ y comparar con una distribución de Poisson.

*Nota: usar la distribución exacta sin ajustar los datos*.
"""
import numpy as np
import pandas as pd
from scipy.stats import poisson
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(42)


class CalcularZ:
    """Simulacion de suma de variables de Bernoulli, cuya cantidad sigue una distribucion de Poisson."""

    def __init__(self, mu=10, p=0.7):
        self.mu = mu
        self.p = p

    def __call__(self):
        k = np.random.poisson(lam=self.mu)
        z = np.random.binomial(n=1, p=self.p, size=k).sum()
        return {
            "z": z,
            "k": k,
        }


def distribucion_poisson(mu=10, k_max=100):
    """Distribucion de Poisson."""
    k = np.arange(k_max + 1)
    return k, poisson(mu=mu).pmf(k)


def ej10():
    """Ejercicio 10."""
    mu = 10
    n_ensemble = 1000
    fig = make_subplots(rows=1, cols=2, shared_yaxes=True)
    for i, p in enumerate([0.7, 1]):
        resultados = []
        for _ in range(n_ensemble):
            juego = CalcularZ(mu=mu, p=p)
            resultados.append(juego())
        resultados = pd.DataFrame(resultados)
        fig.add_trace(
            go.Histogram(
                x=resultados["z"], histnorm="probability", name=f"Simulación con p={p}"
            ),
            row=1,
            col=i + 1,
        )
        k, dist = distribucion_poisson(mu=mu)
        fig.add_trace(
            go.Scatter(x=k, y=dist, name=f"Poiss(mu={mu})"),
            row=1,
            col=i + 1,
        )
        fig.update_xaxes(
            title_text="Ocurrencias",
            range=[0, 30],
            row=1,
            col=i + 1,
        )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text="Calcular la variable aleatoria Z",
        yaxis_title_text="Probabilidad",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej10()
