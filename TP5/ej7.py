"""Ejercicio 7 (Para entregar)"""
import numpy as np
from scipy.stats import norm
from matplotlib.path import Path
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

np.random.seed(42)


def get_MLE(k, n):
    """Retorna el estimador de maximum likelihood de p."""
    return k / n


def get_bound(q, estimator, n):
    """Calcula uno de los límites del intervalo de confianza simétrico (semiancho)."""
    return q * np.sqrt(estimator * (1 - estimator) / n)


def get_corrected_statistic(k, n):
    """Retorna estadistica corregida para el estimador de p."""
    return (k + 2) / (n + 4)


def plot_ej7(n, p, n_realizaciones, CL):
    """Grafica Ejercicio 7."""
    k = np.random.binomial(n, p, size=n_realizaciones)
    q = norm.ppf((CL * 0.01 + 1.0) * 0.5)
    p_MLE = get_MLE(k, n)
    limite_parabolico = get_bound(q, p_MLE, n)
    p_corregido = get_corrected_statistic(k, n)
    limite_corregido = get_bound(q, p_corregido, n)
    sns.set_context("paper", font_scale=1.5)
    fig, (ax1, ax2) = plt.subplots(figsize=(12, 8), nrows=2, sharex=True)
    realizacion = np.arange(1, n_realizaciones + 1)
    pertenece_parabolico = np.abs(p - p_MLE) <= limite_parabolico
    color_parabolico = np.where(pertenece_parabolico, "g", "r")
    cobertura_parabolica = 100.0 * pertenece_parabolico.sum() / n_realizaciones
    ax1.scatter(realizacion, p_MLE, color=color_parabolico, alpha=0.5)
    ax1.hlines(p, 1, n_realizaciones, colors="k", lw=2, ls="dashed", alpha=0.9)
    ax1.text(
        0.05,
        0.9,
        f"Cobertura {cobertura_parabolica:.0f}%",
        ha="left",
        va="top",
        transform=ax1.transAxes,
        bbox={"facecolor": "white"},
    )
    pertenece_corregido = np.abs(p - p_MLE) <= limite_corregido
    color_corregido = np.where(pertenece_corregido, "g", "r")
    cobertura_corregida = 100.0 * pertenece_corregido.sum() / n_realizaciones
    ax2.scatter(realizacion, p_corregido, color=color_corregido, alpha=0.5)
    ax2.hlines(p, 1, n_realizaciones, colors="k", lw=2, ls="dashed", alpha=0.9)
    ax2.text(
        0.05,
        0.9,
        f"Cobertura {cobertura_corregida:.0f}%",
        ha="left",
        va="top",
        transform=ax2.transAxes,
        bbox={"facecolor": "white"},
    )
    fig.supylabel(r"Estimador $\hat{p}$ con errores parabólicos")
    ax1.set_ylabel(r"MLE $\hat{p} = \frac{k}{n}$")
    ax2.set_ylabel(r"Corrección $\hat{p} = \frac{k+2}{n+4}$")
    plt.xlabel("Realizaciones")
    handles = [
        Line2D([0], [0], color="g", alpha=0.9, linewidth=0, marker="o"),
        Line2D([0], [0], color="r", alpha=0.9, linewidth=0, marker="o"),
        Line2D([0], [0], color="k", alpha=0.9, ls="dashed"),
    ]
    labels = [r"Incluye a $p$", r"No incluye a $p$", r"Parámetro $p$"]
    ax1.legend(handles, labels, ncol=3, loc="upper right")
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()
    plt.close()


def ej7():
    """Ejercicio 7."""
    n = widgets.IntSlider(description="n", value=32, min=1, max=512, step=1)
    p = widgets.FloatSlider(description="p", value=0.2, min=0.01, max=0.99, step=0.01)
    n_realizaciones = widgets.IntSlider(
        description="n_realizaciones", value=10000, min=1000, max=10000, step=1000
    )
    CL = widgets.FloatSlider(description="CL", value=95.0, min=1.0, max=99.0, step=1.0)
    parameters = {
        "n": n,
        "p": p,
        "n_realizaciones": n_realizaciones,
        "CL": CL,
    }
    out = widgets.interactive_output(plot_ej7, parameters)
    title = widgets.Label(
        "Seleccionar parámetros",
        layout=widgets.Layout(display="flex", justify_content="center"),
    )
    sliders = [title, *parameters.values()]
    display(
        widgets.HBox(
            [out, widgets.VBox(sliders)],
            layout=widgets.Layout(width="100%", display="flex", align_items="center"),
        )
    )


if __name__ == "__main__":
    ej7()
