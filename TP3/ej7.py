"""Ejercicio 7 (Para entregar)"""
import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

np.random.seed(42)


def get_Sigma_X(sigma1, sigma2, rho):
    """Retorna la matriz de covarianza."""
    return np.array(
        [[sigma1 ** 2, rho * sigma1 * sigma2], [rho * sigma1 * sigma2, sigma2 ** 2]]
    )


def get_mu_X(mu1, mu2):
    """Retorna vector de medias."""
    return np.array([mu1, mu2])


def get_mu_2_prime(x1, mu1, mu2, sigma1, sigma2, rho):
    """Retorna la media de la distribucion condicional."""
    return mu2 + rho * (x1 - mu1) * sigma2 / sigma1


def get_sigma_2_prime(sigma2, rho):
    """Retorna la varianza de la distribucion condicional."""
    return np.sqrt((1 - rho ** 2) * sigma2 ** 2)


def get_x1_x2(mu1, mu2, sigma1, sigma2, rho, n):
    """Genera variable aleatoria (x1, x2) binormal."""
    x1 = np.random.normal(size=n, loc=mu1, scale=sigma1)
    x2 = np.random.normal(
        loc=get_mu_2_prime(x1, mu1, mu2, sigma1, sigma2, rho),
        scale=get_sigma_2_prime(sigma2, rho),
    )
    return x1, x2


def plot_ej7(mu1, mu2, sigma1, sigma2, rho, n, r):
    """Grafica Ejercicio 7."""
    x1, x2 = get_x1_x2(mu1=mu1, mu2=mu2, sigma1=sigma1, sigma2=sigma2, rho=rho, n=n)
    Sigma_X = get_Sigma_X(sigma1=sigma1, sigma2=sigma2, rho=rho)
    mu_X = get_mu_X(mu1=mu1, mu2=mu2)
    L = np.linalg.cholesky(Sigma_X)
    t = np.linspace(0, 2 * np.pi, 1000)
    c = np.column_stack([np.cos(t), np.sin(t)])
    e = r * c @ L.T + mu_X
    porcentaje = Path(e).contains_points(np.column_stack([x1, x2])).sum() / n * 100.0
    probabilidad = (1 - np.exp(-0.5 * r ** 2)) * 100.0
    sns.set_context("paper", font_scale=1.5)
    g = sns.jointplot(x=x1, y=x2, alpha=5 / np.sqrt(n), height=8)
    ax = g.ax_joint
    ax.plot(*e.T, alpha=0.9, c="k")
    text = (
        rf"Superficie {r}$\sigma$"
        "\n"
        f"Porcentaje de puntos {porcentaje:.2f}%"
        "\n"
        f"Probabilidad exacta {probabilidad:.2f}%"
    )
    ax.text(x=0.05, y=1.0, s=text, ha="left", va="top", transform=ax.transAxes)
    ax.set_xlim(-1, 5.5)
    ax.set_ylim(-1.5, 4.5)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    plt.show()
    plt.close()


def ej7():
    """Ejercicio 7."""
    mu1 = widgets.FloatSlider(description="mu1", value=2.3, min=-0.5, max=5.0)
    mu2 = widgets.FloatSlider(description="mu2", value=1.5, min=-0.5, max=5.0)
    sigma1 = widgets.FloatSlider(description="sigma1", value=1.2, min=0.1, max=2.0)
    sigma2 = widgets.FloatSlider(description="sigma2", value=0.5, min=0.1, max=2.0)
    rho = widgets.FloatSlider(description="rho", value=0.7, min=-0.9, max=0.9)
    n = widgets.IntSlider(description="n", value=1000, min=1000, max=10000, step=1000)
    r = widgets.FloatSlider(description="r", value=1.0, min=0.5, max=4.0, step=0.5)
    out = widgets.interactive_output(
        plot_ej7,
        {
            "mu1": mu1,
            "mu2": mu2,
            "sigma1": sigma1,
            "sigma2": sigma2,
            "rho": rho,
            "n": n,
            "r": r,
        },
    )
    title = widgets.Label(
        "Seleccionar parámetros",
        layout=widgets.Layout(display="flex", justify_content="center"),
    )
    sliders = [title, mu1, mu2, sigma1, sigma2, rho, n, r]
    display(
        widgets.HBox(
            [out, widgets.VBox(sliders)],
            layout=widgets.Layout(width="100%", display="flex", align_items="center"),
        )
    )


if __name__ == "__main__":
    ej7()
