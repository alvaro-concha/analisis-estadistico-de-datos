"""Ejercicio 8: El jugador de dardos torpe"""
import numpy as np
import pandas as pd
from scipy.stats import poisson
import plotly.graph_objects as go
from plotly.subplots import make_subplots

np.random.seed(42)


class LanzarDardos:
    """Simulacion de lanzamiento de dardos."""

    def __init__(self, r_doble=170, r_int=12.7, r_ext=31.8, n_lanzamientos=100):
        self.r_doble = r_doble
        self.r_int = r_int
        self.r_ext = r_ext
        self.n_lanzamientos = n_lanzamientos

    def __call__(self):
        length = self.r_doble * np.sqrt(
            np.random.uniform(0, 1, size=self.n_lanzamientos)
        )
        angle = np.pi * np.random.uniform(0, 2, size=self.n_lanzamientos)
        shots = np.column_stack([length * np.cos(angle), length * np.sin(angle)])
        dists = np.linalg.norm(shots, axis=1)
        return {
            "k": np.logical_and(dists <= self.r_ext, dists >= self.r_int).sum(),
            "shots": shots,
        }


def distribucion_poisson(r_doble=170, r_int=12.7, r_ext=31.8, n_lanzamientos=100):
    """Distribucion exacta (Poisson), del problema de lanzamiento de dardos."""
    mu = n_lanzamientos * (r_ext ** 2 - r_int ** 2) / r_doble ** 2
    print(f"Promedio teorico {mu:.2f}")
    k = np.arange(n_lanzamientos)
    return k, poisson(mu=mu).pmf(k)


def ej8():
    """Ejercicio 8."""
    r_doble = 170
    r_int = 12.7
    r_ext = 31.8
    n_ensemble = 1000
    resultados = []
    for _ in range(n_ensemble):
        juego = LanzarDardos()
        resultados.append(juego())
    resultados = pd.DataFrame(resultados)
    print(f'Promedio simulacion {resultados["k"].mean():.2f}')
    k, dist = distribucion_poisson()
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Histogram(
            x=resultados["k"],
            histnorm="probability",
            name="Simulación",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(go.Scatter(x=k, y=dist, name="Poisson"), row=1, col=1)
    fig.update_traces(opacity=0.75)
    fig.update_xaxes(
        title_text="Ocurrencias",
        row=1,
        col=1,
    )
    fig.update_yaxes(
        title_text="Probabilidad",
        row=1,
        col=1,
    )
    fig.update_xaxes(range=[0, 13], row=1, col=1)

    shots = np.concatenate(resultados["shots"])
    idx = np.random.choice(len(shots), size=1000, replace=False)
    fig.add_trace(
        go.Scatter(
            x=shots[idx, 0], y=shots[idx, 1], opacity=0.75, mode="markers", name="Tiros"
        ),
        row=1,
        col=2,
    )
    fig.add_shape(
        type="circle",
        xref="x",
        yref="y",
        x0=-r_doble,
        y0=-r_doble,
        x1=r_doble,
        y1=r_doble,
        row=1,
        col=2,
    )
    fig.add_shape(
        type="circle",
        xref="x",
        yref="y",
        x0=-r_int,
        y0=-r_int,
        x1=r_int,
        y1=r_int,
        row=1,
        col=2,
    )
    fig.add_shape(
        type="circle",
        xref="x",
        yref="y",
        x0=-r_ext,
        y0=-r_ext,
        x1=r_ext,
        y1=r_ext,
        row=1,
        col=2,
    )
    fig.update_xaxes(
        title_text="x (mm)",
        row=1,
        col=2,
    )
    fig.update_yaxes(
        title_text="y (mm)",
        row=1,
        col=2,
    )
    fig.update_layout(
        width=1200, height=600, title_text="El jugador de dardos torpe", bargap=0.2
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej8()
