"""Ejercicio 7 (Para entregar)"""
import numpy as np
from scipy.stats import chi2, norm, normaltest
from scipy.integrate import romb
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
                # {"yaxis": dict(range=None)},
            ],
        )
        step["args"][0]["visible"][3 * idx] = True
        step["args"][0]["visible"][3 * idx + 1] = True
        step["args"][0]["visible"][3 * idx + 2] = True
        # if k == 1:
        #     max_y_axis = 1.0
        #     step["args"][1] = {"yaxis": dict(range=[-max_y_axis / 20, max_y_axis])}
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


def graficar_ej7_distribuciones(ks, resultados, n_ensemble, n_bines):
    """Graficar las distribuciones del ejercicio 7."""
    fig = go.Figure()
    for k in ks:
        valor_max = resultados[k].max()
        valor_min = resultados[k].min()
        dx = (valor_max - valor_min) / n_bines
        histograma_frecuencia, bin_edges = np.histogram(
            resultados[k], bins=n_bines, range=(valor_min, valor_max), density=False
        )
        valores = (bin_edges[:-1] + bin_edges[1:]) * 0.5
        fig.add_trace(
            go.Bar(
                x=valores,
                y=histograma_frecuencia,
                name=f"Simulación con k={k}",
                visible=False,
            )
        )
        distribucion_chi2 = chi2.pdf(x=valores, df=k)
        fig.add_trace(
            go.Scatter(
                x=valores,
                y=distribucion_chi2 * n_ensemble * dx,
                name=f"Chi-cuadrado(k={k})",
                visible=False,
            )
        )
        distribucion_norm = norm.pdf(x=valores, loc=k, scale=np.sqrt(2 * k))
        fig.add_trace(
            go.Scatter(
                x=valores,
                y=distribucion_norm * n_ensemble * dx,
                name=f"Normal(media={k}, varianza={2*k})",
                visible=False,
            )
        )
    fig.update_xaxes(
        title_text="Eventos",
    )
    fig.update_yaxes(
        title_text="Frecuencia",
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text=f"Simulación de la variable aleatoria Z, con diferentes grados de libertad",
        bargap=0.2,
    )
    graficar_slider(fig, ks=ks)
    fig.show(renderer="notebook")


def graficar_ej7_tests(ks, statistics, p_values):
    """Graficar los resultados de los tests del ejercicio 7."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=ks,
            y=statistics,
            mode="lines",
            name="Statistic",
            line_color="blue",
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=ks,
            y=p_values,
            mode="lines",
            name="p-value",
            line_color="red",
        ),
        secondary_y=True,
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        title_text="Test de normalidad D'Agostino-Pearson, basado en la asimetría y kurotsis de la muestra",
    )
    fig.update_xaxes(
        title_text="Grados de libertad",
        type="log",
    )
    fig.update_yaxes(
        title_text="Statistic",
        secondary_y=False,
        titlefont_color="blue",
        tickfont_color="blue",
        type="log",
    )
    fig.update_yaxes(
        title_text="p-value",
        secondary_y=True,
        titlefont_color="red",
        tickfont_color="red",
        type="log",
    )
    fig.show(renderer="notebook")


def ej7():
    """Ejercicio 7."""
    ks = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 100, 500, 1000]
    n_ensemble = 10000
    n_bines = 100
    resultados = {}
    statistics = []
    p_values = []
    for k in ks:
        x = np.random.normal(size=(n_ensemble, k))
        y = x ** 2
        z = y.sum(axis=1)
        resultados[k] = z
        stat, p_value = normaltest(a=z)
        statistics.append(stat)
        p_values.append(p_value)
    graficar_ej7_distribuciones(
        ks=ks, resultados=resultados, n_ensemble=n_ensemble, n_bines=n_bines
    )
    graficar_ej7_tests(ks=ks, statistics=statistics, p_values=p_values)


if __name__ == "__main__":
    ej7()
