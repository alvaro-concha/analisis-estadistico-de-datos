"""Ejercicio 5"""
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display


def plot_ej5(n, k):
    """Grafica Ejercicio 5."""
    p_lims = (1e-6, 1.0 - 1e-6)
    ps = np.linspace(*p_lims, 1000)
    p_MLE = k / n

    def J(ps, n, k):
        return -2.0 * (
            k * np.log(n * ps / k) + (n - k) * np.log((1 - ps) / (1 - k / n))
        )

    plt.plot(ps, J(ps, n, k))
    plt.scatter(p_MLE, J(p_MLE, n, k))
    plt.xlabel(r"$p$")
    plt.ylabel(r"Función de costo $J(p)$")
    plt.xlim(*p_lims)
    plt.ylim(-10.0, 100.0)
    plt.show()
    plt.close()


def ej5():
    """Ejercicio 5."""
    n = widgets.IntSlider(description="n", value=12, min=8, max=100, step=1)
    k = widgets.IntSlider(description="k", value=8, min=1, max=11, step=1)

    def update_k(*args):
        k.max = n.value - 1

    k.observe(update_k, "value")

    def update_n(*args):
        n.min = k.value + 1

    n.observe(update_n, "value")
    parameters = {
        "n": n,
        "k": k,
    }
    out = widgets.interactive_output(plot_ej5, parameters)
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
    ej5()
