"""Ejercicio 10 (Para entregar)"""
import numpy as np
import pandas as pd
from scipy.stats import poisson
import plotly.graph_objects as go

np.random.seed(42)


class CalcularZ:
    """Simulacion de suma de variables de Bernoulli, cuya cantidad sigue una distribucion de Poisson."""

    def __init__(self, mu=10, p=0.7):
        self.mu = mu
        self.p = p

    def __call__(self):
        k = np.random.poisson(lam=self.mu)
        z = np.random.binomial(n=1, p=self.p, size=k).sum()
        return {"z": z, "k": k, "p": self.p}


def distribucion_poisson(mu=10, k_max=100):
    """Distribucion de Poisson."""
    k = np.arange(k_max + 1)
    return k, poisson(mu=mu).pmf(k)


def graficar_slider(fig, ps):
    """Crear un slider para un conjunto de figuras."""
    fig.data[0].visible = True
    fig.data[1].visible = True
    steps = []
    for i in range(len(ps)):
        step = dict(
            method="update",
            args=[
                {"visible": [False] * len(fig.data)},
                {"label": f"p={ps[i]:.1f}"},
            ],
        )
        step["args"][0]["visible"][2 * i] = True
        step["args"][0]["visible"][2 * i + 1] = True
        step["args"][0]["visible"][-1] = True
        steps.append(step)

    sliders = [
        dict(
            currentvalue={"prefix": "p = "},
            steps=steps,
            pad={"t": 50},
        )
    ]

    fig.update_layout(
        sliders=sliders,
    )
    for i, p in enumerate(ps):
        fig["layout"]["sliders"][0]["steps"][i]["label"] = f"{p:.1f}"


def graficar_ej10(mu, ps, resultados):
    """Graficar el ejercicio 10."""
    fig = go.Figure()
    for p in ps:
        fig.add_trace(
            go.Histogram(
                x=resultados[resultados["p"] == p]["z"],
                histnorm="probability",
                name=f"Simulación con p={p:.1f}",
                visible=False,
            )
        )
        k, dist = distribucion_poisson(mu=p * mu)
        fig.add_trace(go.Scatter(x=k, y=dist, name="Poisson(p mu)", visible=False))
    k, dist = distribucion_poisson(mu=mu)
    fig.add_trace(go.Scatter(x=k, y=dist, name="Poisson(mu)"))
    fig.update_xaxes(
        title_text="Eventos",
        range=[0, 30],
    )
    fig.update_yaxes(
        title_text="Probabilidad",
        range=[0, 0.4],
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text=f"Simulación de la variable aleatoria Z, usando mu={mu} y diferentes valores de p",
        bargap=0.2,
    )
    graficar_slider(fig, ps=ps)
    fig.show(renderer="notebook")


def ej10():
    """Ejercicio 10."""
    mu = 10
    ps = np.linspace(0.1, 1.0, 10)
    n_ensemble = 1000
    resultados = []
    for p in ps:
        for _ in range(n_ensemble):
            juego = CalcularZ(mu=mu, p=p)
            resultados.append(juego())
    resultados = pd.DataFrame(resultados)
    graficar_ej10(mu=mu, ps=ps, resultados=resultados)


if __name__ == "__main__":
    ej10()
