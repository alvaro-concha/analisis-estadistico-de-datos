"""Ejercicio 6"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display


def plot_ej6(x1, x2, x3, sigma):
    """Grafica Ejercicio 6."""
    mu_lims = (-20.0, 20.0)
    mus = np.linspace(*mu_lims, 1000)
    mu_MLE = np.mean([x1, x2, x3])

    def J(mus, sigma, mu_MLE):
        return 3 * ((mus - mu_MLE) / sigma) ** 2

    plt.plot(mus, J(mus, sigma, mu_MLE))
    plt.scatter(mu_MLE, J(mu_MLE, sigma, mu_MLE))
    plt.xlabel(r"$\mu$")
    plt.ylabel(r"Función de costo $J(\mu)$")
    plt.xlim(*mu_lims)
    plt.ylim(-1.0, 19.0)
    plt.show()
    plt.close()


def ej6():
    """Ejercicio 6."""
    x1 = widgets.FloatSlider(
        description="x1", value=3.38, min=-13.38, max=13.38, step=1.0
    )
    x2 = widgets.FloatSlider(
        description="x2", value=5.06, min=-15.06, max=15.06, step=1.0
    )
    x3 = widgets.FloatSlider(
        description="x3", value=7.67, min=-17.67, max=17.67, step=1.0
    )
    sigma = widgets.FloatSlider(
        description="sigma", value=1.4, min=0.4, max=11.4, step=1.0
    )
    parameters = {
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "sigma": sigma,
    }
    out = widgets.interactive_output(plot_ej6, parameters)
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
    ej6()
