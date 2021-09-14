"""Ejercicio 7 (Para entregar)"""
import numpy as np
from scipy.stats import chi2, norm
import plotly.graph_objects as go

np.random.seed(42)


def graficar_slider(fig, ks):
    """Crear un slider para un conjunto de figuras."""
    default_idx = 6
    fig.data[3 * default_idx].visible = True
    fig.data[3 * default_idx + 1].visible = True
    fig.data[3 * default_idx + 2].visible = True
    steps = []
    for idx, k in enumerate(ks):
        step = dict(
            method="update",
            args=[
                {"visible": [False] * len(fig.data)},
                {"yaxis": dict(range=None)},
            ],
        )
        step["args"][0]["visible"][3 * idx] = True
        step["args"][0]["visible"][3 * idx + 1] = True
        step["args"][0]["visible"][3 * idx + 2] = True
        if k == 1:
            max_y_axis = 1.0
            step["args"][1] = {"yaxis": dict(range=[-max_y_axis / 20, max_y_axis])}
        steps.append(step)
    sliders = [
        dict(
            currentvalue={"prefix": "Grados de libertad k="},
            steps=steps,
            pad={"t": 50},
            active=default_idx,
        )
    ]
    fig.update_layout(
        sliders=sliders,
    )
    for i, k in enumerate(ks):
        fig["layout"]["sliders"][0]["steps"][i]["label"] = f"{k}"


def graficar_ej7(ks, resultados):
    """Graficar el ejercicio 7."""
    fig = go.Figure()
    for k in ks:
        fig.add_trace(
            go.Histogram(
                x=resultados[k],
                histnorm="probability density",
                name=f"Simulación con k={k}",
                visible=False,
            )
        )
        valores = np.linspace(resultados[k].min(), resultados[k].max(), 100)
        distribucion_chi2 = chi2.pdf(x=valores, df=k)
        fig.add_trace(
            go.Scatter(
                x=valores,
                y=distribucion_chi2,
                name=f"Chi-cuadrado(k={k})",
                visible=False,
            )
        )
        distribucion_norm = norm.pdf(x=valores, loc=k, scale=np.sqrt(2 * k))
        fig.add_trace(
            go.Scatter(
                x=valores,
                y=distribucion_norm,
                name=f"Normal(media={k}, varianza={2*k})",
                visible=False,
            )
        )
    fig.update_xaxes(
        title_text="Eventos",
    )
    fig.update_yaxes(
        title_text="Densidad de probabilidad",
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text=f"Simulación de la variable aleatoria Z, con diferentes grados de libertad",
        bargap=0.2,
    )
    graficar_slider(fig, ks=ks)
    fig.show(renderer="notebook")


def ej7():
    """Ejercicio 7."""
    ks = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 1000]
    n_ensemble = 10000
    resultados = {}
    for k in ks:
        x = np.random.normal(size=(n_ensemble, k))
        y = x ** 2
        z = y.sum(axis=1)
        resultados[k] = z
    graficar_ej7(ks=ks, resultados=resultados)


if __name__ == "__main__":
    ej7()
