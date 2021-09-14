"""Ejercicio 5"""
from math import ceil
import numpy as np
from scipy.stats import norm
import plotly.graph_objects as go

np.random.seed(42)


def ej5():
    """Ejercicio 5."""
    n_ensemble = 1000
    n_variables = 10
    mu = 1.7
    x = np.random.poisson(lam=mu, size=(n_ensemble, n_variables))
    y = x.sum(axis=1)
    bin_width = 2
    max_val = bin_width * ceil(y.max() / bin_width)
    n_bins = max_val // bin_width
    hist, bin_edges = np.histogram(y, bins=n_bins, range=(0, max_val), density=True)
    valores = (bin_edges[:-1] + bin_edges[1:]) * 0.5
    media = n_variables * mu
    varianza = media
    gauss = norm.pdf(x=valores, loc=media, scale=np.sqrt(varianza))
    fig = go.Figure(
        [
            go.Bar(x=valores, y=hist, name="Histograma"),
            go.Scatter(x=valores, y=gauss, mode="lines", name="Gaussiana"),
        ]
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        xaxis_title_text="Eventos",
        yaxis_title_text="Densidad de probabilidad",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej5()
