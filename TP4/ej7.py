"""Ejercicio 7 (Para entregar)"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display


def get_Sigma(sigma1, sigma2, rho):
    """Retorna la matriz de covarianza."""
    return np.array(
        [[sigma1 ** 2, rho * sigma1 * sigma2], [rho * sigma1 * sigma2, sigma2 ** 2]]
    )


def get_J(mus, Sigma_inv, x):
    """Retorna la funcion de costo."""
    return np.sum(
        (x[:, np.newaxis] - mus).T @ Sigma_inv * (x[:, np.newaxis] - mus).T, axis=1
    )


def plot_ej7(sigma1, sigma2, rho, x1, x2):
    """Grafica Ejercicio 7."""
    num_grid = 100
    mu1_lims = (-2.5, 17.5)
    mu2_lims = (2.5, 22.5)
    mu1 = np.linspace(*mu1_lims, num_grid)
    mu2 = np.linspace(*mu2_lims, num_grid)
    mus = np.meshgrid(mu1, mu2)
    mus = np.vstack([mus[0].ravel(), mus[1].ravel()])
    Sigma = get_Sigma(sigma1=sigma1, sigma2=sigma2, rho=rho)
    x = np.array([x1, x2])
    J = get_J(mus=mus, Sigma_inv=np.linalg.inv(Sigma), x=x)
    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    J = J.reshape((num_grid, num_grid))
    mus = mus.reshape((2, num_grid, num_grid))
    contour = plt.contour(
        *mus, J, levels=(1, 4, 9, 16), colors=["r", "g", "b", "brown"]
    )
    plt.clabel(contour)
    plt.scatter(x1, x2, c="k", s=1)
    plt.text(x1, x2, "0", ha="center", va="center")
    plt.title(r"Función de costo $J(\mathbf{\mu})$")
    plt.xlim(*mu1_lims)
    plt.ylim(*mu2_lims)
    plt.xlabel(r"$\mu_1$")
    plt.ylabel(r"$\mu_2$")
    plt.show()
    plt.close()


def ej7():
    """Ejercicio 7."""
    sigma1 = widgets.FloatSlider(description="sigma1", value=2.3, min=0.1, max=3.0)
    sigma2 = widgets.FloatSlider(description="sigma2", value=1.7, min=0.1, max=3.0)
    rho = widgets.FloatSlider(
        description="rho", value=-0.78, min=-0.99, max=0.99, step=0.01
    )
    x1 = widgets.FloatSlider(description="x1", value=7.9, min=0.1, max=20.0)
    x2 = widgets.FloatSlider(description="x2", value=13.4, min=0.1, max=20.0)
    parameters = {
        "sigma1": sigma1,
        "sigma2": sigma2,
        "rho": rho,
        "x1": x1,
        "x2": x2,
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
