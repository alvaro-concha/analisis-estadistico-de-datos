"""Ejercicio 4"""
import numpy as np
from scipy.stats import uniform
import plotly.graph_objects as go

np.random.seed(42)


def ej4():
    """Ejercicio 4."""
    a = 0
    b = 25
    uniforme = uniform(loc=a, scale=b)
    n_eventos = 1000
    x = uniforme.rvs(size=n_eventos)
    n_bines = 10
    histograma_frecuencia = (
        np.histogram(x, bins=n_bines, range=(a, b), density=False)[0] / n_eventos
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
    fig = go.Figure(
        [
            go.Bar(x=valores, y=histograma_frecuencia, name="Histograma de frecuencia"),
            go.Bar(x=valores, y=histograma_densidad, name="Histograma de densidad"),
            go.Scatter(
                x=valores, y=distribucion, mode="lines", name="Distribución uniforme"
            ),
        ]
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        xaxis_title_text="Eventos",
        yaxis_title_text="Densidad de probabilidad o frecuencia",
        bargap=0.2,
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej4()
