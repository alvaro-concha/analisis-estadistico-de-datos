"""Ejercicio 3"""
import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

np.random.seed(42)


def plot_ej3(n_realizaciones, n, delta):
    """Grafica Ejercicio 3."""
    x = np.random.normal(size=(n_realizaciones, n))
    varianza = np.var(x, axis=1, ddof=delta)
    x_lims = (0.0, 10.0)
    valores = np.linspace(*x_lims, 1000)
    distribucion = chi2(df=n - 1, scale=1.0 / (n - delta)).pdf(x=valores)
    sns.set_context("paper", font_scale=1.5)
    plt.figure(figsize=(8, 4))
    plt.hist(varianza, bins="auto", density=True, alpha=0.9, label="Histograma")
    plt.plot(valores, distribucion, alpha=0.9, label="Distribución")
    text = (
        f"Sesgo histograma {(varianza.mean() - 1.0):.2f}"
        "\n"
        f"Sesgo teórico        {((delta - 1) / (n - delta)):.2f}"
        "\n"
        f"Varianza histograma {(varianza.var()):.2f}"
        "\n"
        f"Varianza teórica        {(2.0 * (n - 1) / ((n - delta) ** 2)):.2f}"
    )
    plt.text(
        x=0.99, y=0.99, s=text, ha="right", va="top", transform=plt.gca().transAxes
    )
    plt.legend(loc="upper left")
    plt.xlabel(r"$s_{n - \delta}^2$")
    plt.ylabel("Densidad de probabilidad")
    plt.xlim(*x_lims)
    plt.ylim(0.0, 4.0)
    plt.show()
    plt.close()


def ej3():
    """Ejercicio 3."""
    n_realizaciones = widgets.IntSlider(
        description="n_realizaciones", value=1000, min=1000, max=10000, step=1000
    )
    n = widgets.IntSlider(description="n", value=2, min=2, max=100, step=1)
    delta = widgets.Dropdown(description="delta", value=0, options=np.arange(2))

    def update_delta(*args):
        delta.options = np.arange(n.value)

    delta.observe(update_delta, "value")
    parameters = {
        "n_realizaciones": n_realizaciones,
        "n": n,
        "delta": delta,
    }
    out = widgets.interactive_output(plot_ej3, parameters)
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
    ej3()
