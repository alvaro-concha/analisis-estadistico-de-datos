"""Ejercicio 6"""
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

np.random.seed(42)


def ej6():
    """Ejercicio 6."""
    n_eventos = 1000
    x = np.random.normal(size=n_eventos)
    valores = np.linspace(x.min(), x.max(), 100)
    acumulada = norm.cdf(x=valores)
    fig = go.Figure(
        [
            go.Histogram(
                x=x,
                histnorm="probability density",
                cumulative_enabled=True,
                name="Histograma acumulado",
            ),
            go.Scatter(x=valores, y=acumulada, mode="lines", name="Densidad acumulada"),
        ]
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        xaxis_title_text="Eventos",
        yaxis_title_text="Densidad de probabilidad acumulada",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej6()
