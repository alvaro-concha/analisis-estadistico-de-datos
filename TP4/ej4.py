"""Ejercicio 4"""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display


def plot_ej4(x, sigma):
    """Grafica Ejercicio 4."""
    mu_lims = (-100.0, 100.0)
    mus = np.linspace(*mu_lims, 1000)
    mu_MLE = x

    def J(mus, sigma, x):
        return ((x - mus) / sigma) ** 2

    plt.plot(mus, J(mus, sigma, x))
    plt.scatter(mu_MLE, J(mu_MLE, sigma, x))
    plt.xlabel(r"$\mu$")
    plt.ylabel(r"Función de costo $J(\mu)$")
    plt.xlim(*mu_lims)
    plt.ylim(-1.0, 19.0)
    plt.show()
    plt.close()


def ej4():
    """Ejercicio 4."""
    x = widgets.FloatSlider(
        description="x", value=37.2, min=-107.2, max=107.2, step=10.0
    )
    sigma = widgets.FloatSlider(
        description="sigma", value=4.5, min=0.5, max=105.0, step=1.0
    )
    parameters = {
        "x": x,
        "sigma": sigma,
    }
    out = widgets.interactive_output(plot_ej4, parameters)
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
    ej4()
