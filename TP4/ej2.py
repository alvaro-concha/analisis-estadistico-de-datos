"""Ejercicio 2"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

np.random.seed(42)


def plot_ej2(n_realizaciones, n):
    """Grafica Ejercicio 2."""
    x = np.random.normal(size=(n_realizaciones, n))
    media = np.mean(x, axis=1)
    x_lims = (-4.0, 4.0)
    valores = np.linspace(*x_lims, 1000)
    distribucion = norm(loc=0, scale=1 / np.sqrt(n)).pdf(x=valores)
    sns.set_context("paper", font_scale=1.5)
    plt.figure(figsize=(8, 4))
    plt.hist(media, density=True, alpha=0.9, label="Histograma")
    plt.plot(valores, distribucion, alpha=0.9, label="Distribución")
    plt.legend()
    plt.xlabel(r"$\bar{X}$")
    plt.ylabel("Densidad de probabilidad")
    plt.xlim(*x_lims)
    plt.ylim(0, 4.0)
    plt.show()
    plt.close()


def ej2():
    """Ejercicio 2."""
    n_realizaciones = widgets.IntSlider(
        description="n_realizaciones", value=1000, min=1000, max=10000, step=1000
    )
    n = widgets.IntSlider(description="n", value=3, min=1, max=100, step=1)
    parameters = {
        "n_realizaciones": n_realizaciones,
        "n": n,
    }
    out = widgets.interactive_output(plot_ej2, parameters)
    title = widgets.Label(
        "Seleccionar parámetros",
        layout=widgets.Layout(display="flex", justify_content="center"),
    )
    sliders = [title, *parameters.values(), out]
    display(
        widgets.VBox(
            sliders,
            layout=widgets.Layout(width="100%", display="flex", align_items="center"),
        )
    )


if __name__ == "__main__":
    ej2()
