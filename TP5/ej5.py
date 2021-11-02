"""Ejercicio 5"""
import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

np.random.seed(42)


def get_cov(sigma1, sigma2, rho):
    """Calcula matriz de covarianza."""
    return np.array(
        [[sigma1 ** 2, rho * sigma1 * sigma2], [rho * sigma1 * sigma2, sigma2 ** 2]]
    )


def get_mu(mu1, mu2):
    """Retorna vector de medias."""
    return np.array([mu1, mu2])


def plot_ej5(mu1, mu2, sigma1, sigma2, rho, n, CL):
    """Grafica Ejercicio 5."""
    mu = get_mu(mu1=mu1, mu2=mu2)
    cov = get_cov(sigma1=sigma1, sigma2=sigma2, rho=rho)
    x1, x2 = np.random.multivariate_normal(mean=mu, cov=cov, size=n).T
    L = np.linalg.cholesky(cov)
    t = np.linspace(0, 2 * np.pi, 1000)
    r = np.sqrt(-2 * np.log(1 - CL * 0.01))
    circulo = np.column_stack([np.cos(t), np.sin(t)])
    elipse = r * circulo @ L.T + mu
    probabilidad_aproximada = (
        Path(elipse).contains_points(np.column_stack([x1, x2])).sum() / n * 100.0
    )
    sns.set_context("paper", font_scale=1.5)
    g = sns.jointplot(x=x1, y=x2, alpha=5 / np.sqrt(n), height=8)
    ax = g.ax_joint
    ax.plot(*elipse.T, alpha=0.9, c="k")
    ax.scatter(*mu, alpha=0.9, c="k")
    text = (
        rf"Tamaño de la elipse            {r:.1f}$\sigma$"
        "\n"
        f"Nivel de confianza exacto   {CL:.1f}%"
        "\n"
        f"Cobertura aproximada        {probabilidad_aproximada:.1f}%"
    )
    ax.text(x=0.05, y=1.0, s=text, ha="left", va="top", transform=ax.transAxes)
    ax.set_xlim(3.0, 17.0)
    ax.set_ylim(1.0, 15.0)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    plt.show()
    plt.close()


def ej5():
    """Ejercicio 5."""
    mu1 = widgets.FloatSlider(description="mu1", value=10.7, min=6.0, max=13.0)
    mu2 = widgets.FloatSlider(description="mu2", value=8.3, min=6.0, max=13.0)
    sigma1 = widgets.FloatSlider(description="sigma1", value=1.7, min=0.1, max=3.0)
    sigma2 = widgets.FloatSlider(description="sigma2", value=2.4, min=0.1, max=3.0)
    rho = widgets.FloatSlider(
        description="rho", value=0.78, min=-0.99, max=0.99, step=0.01
    )
    n = widgets.IntSlider(description="n", value=10000, min=1000, max=10000, step=1000)
    CL = widgets.FloatSlider(description="CL", value=95.0, min=1.0, max=99.0, step=1.0)
    parameters = {
        "mu1": mu1,
        "mu2": mu2,
        "sigma1": sigma1,
        "sigma2": sigma2,
        "rho": rho,
        "n": n,
        "CL": CL,
    }
    out = widgets.interactive_output(plot_ej5, parameters)
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
    ej5()
