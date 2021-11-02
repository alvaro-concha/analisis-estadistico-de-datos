"""Ejercicio 6 (Opcional)"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display


def get_mu(S, beta, r):
    """qetorna mu."""
    return S[..., np.newaxis] * np.power(r, -beta[..., np.newaxis])


def get_J(mu, k):
    """qetorna la funcion de costo, J."""
    return 2 * np.sum(mu - k - k * np.log(mu / k), axis=-1)


def plot_ej6(q):
    """Grafica Ejercicio 6."""
    num_grid = 1000
    S_lims = (1e-6, 100.0)
    beta_lims = (-10.0, 10.0)
    S_domain = np.linspace(*S_lims, num_grid)
    beta_domain = np.linspace(*beta_lims, num_grid)
    S, beta = np.meshgrid(S_domain, beta_domain)
    r = np.array([0.764, 1.052, 1.236])
    k = np.array([33.0, 19.0, 11.0])
    mu = get_mu(S, beta, r)
    J = get_J(mu, k)
    J_min_idx = np.argmin(J)
    J_min = J.ravel()[J_min_idx]
    S_MLE = S.ravel()[J_min_idx]
    beta_MLE = beta.ravel()[J_min_idx]
    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    contour = plt.contour(S, beta, J - J_min, levels=(q ** 2,), colors=("white",))
    plt.clabel(contour)
    plt.contourf(S, beta, J, 20, cmap="plasma")
    plt.colorbar()
    plt.scatter(S_MLE, beta_MLE, c="white")
    text = (
        r"$J_{\min} = $" + f"{J_min:.2f}\n"
        r"$S_{MLE} = $" + f"{S_MLE:.1f}\n"
        r"$\beta_{MLE} = $" + f"{beta_MLE:.1f}"
    )
    plt.text(S_MLE + 20, beta_MLE, text, ha="left", va="top", c="white")
    plt.title(r"Función de costo $J(\mathbf{\theta})$")
    plt.xlim(*S_lims)
    plt.ylim(*beta_lims)
    plt.xlabel(r"$S$")
    plt.ylabel(r"$\beta$")
    plt.show()
    plt.close()


def ej6():
    """Ejercicio 6."""
    q = widgets.FloatSlider(description="q", value=1.0, min=0.1, max=50.0)
    parameters = {"q": q}
    out = widgets.interactive_output(plot_ej6, parameters)
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
    ej6()
