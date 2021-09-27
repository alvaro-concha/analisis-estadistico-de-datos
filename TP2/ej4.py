"""Ejercicio 4"""
import numpy as np
from scipy.stats import uniform
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(42)


def ej4():
    """Ejercicio 4."""
    a = 0
    b = 25
    uniforme = uniform(loc=a, scale=b)
    n_eventos = 1000
    x = uniforme.rvs(size=n_eventos)
    n_bines = 10
    histograma_frecuencia, _ = np.histogram(
        x, bins=n_bines, range=(a, b), density=False
    )
    histograma_densidad, bin_edges = np.histogram(
        x, bins=n_bines, range=(a, b), density=True
    )
    valores = (bin_edges[:-1] + bin_edges[1:]) * 0.5
    distribucion = uniforme.pdf(x=valores)
    print(f"Media muestral\t{uniforme.mean():.1f}")
    print(f"Media exacta\t{x.mean():.1f}")
    print(f"Desviacion estandar muestral\t{x.std():.1f}")
    print(f"Desviacion estandar exacta\t{uniforme.std():.1f}")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=valores,
            y=histograma_frecuencia,
            name="Histograma de frecuencia",
            marker_color="blue",
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=valores,
            y=distribucion * n_eventos * (b - a) / n_bines,
            mode="lines",
            name="Frecuencia uniforme",
            line_color="blue",
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Bar(
            x=valores,
            y=histograma_densidad,
            name="Histograma de densidad",
            marker_color="red",
        ),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(
            x=valores,
            y=distribucion,
            mode="lines",
            name="Densidad uniforme",
            line_color="red",
        ),
        secondary_y=True,
    )
    fig.update_traces(opacity=0.5)
    fig.update_layout(
        xaxis_title_text="Eventos",
        bargap=0.2,
    )
    fig.update_yaxes(
        title_text="Frecuencia",
        secondary_y=False,
        titlefont_color="blue",
        tickfont_color="blue",
    )
    fig.update_yaxes(
        title_text="Densidad de probabilidad",
        secondary_y=True,
        titlefont_color="red",
        tickfont_color="red",
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej4()
