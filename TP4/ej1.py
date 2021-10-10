"""Ejercicio 1"""
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


class PlotEj1:
    """Grafica Ejercicio 1."""

    def __init__(self):
        n_eventos = 10000
        t = np.linspace(0, 2 * np.pi, 1000)
        self.x = np.random.normal(size=(n_eventos, 2))
        self.c = np.column_stack([np.cos(t), np.sin(t)])

    def __call__(self, mu1, mu2, sigma1, sigma2, rho, r):
        cov = get_cov(sigma1=sigma1, sigma2=sigma2, rho=rho)
        mu = get_mu(mu1=mu1, mu2=mu2)
        L = np.linalg.cholesky(cov)
        y = self.x @ L.T + mu
        e = r * self.c @ L.T + mu
        porcentaje = Path(e).contains_points(y).sum() / len(y) * 100.0
        sns.set_context("paper", font_scale=1.5)
        g = sns.jointplot(x=y[:, 0], y=y[:, 1], alpha=0.05, height=8)
        g.ax_joint.plot(
            *e.T,
            alpha=0.9,
            c="k",
            label=rf"Superficie {r}$\sigma$, aprox. {porcentaje:.2f}%",
        )
        g.ax_joint.set_xlim(-10, 10)
        g.ax_joint.set_ylim(-10, 10)
        g.ax_joint.set_xlabel(r"$x_1$")
        g.ax_joint.set_ylabel(r"$x_2$")
        g.ax_joint.legend(loc="upper left")
        plt.show()


def ej1():
    """Ejercicio 1."""
    mu1 = widgets.FloatSlider(description="mu1", value=1.3, min=-2.0, max=2.0)
    mu2 = widgets.FloatSlider(description="mu2", value=0.5, min=-2.0, max=2.0)
    sigma1 = widgets.FloatSlider(description="sigma1", value=1.7, min=0.1, max=10.0)
    sigma2 = widgets.FloatSlider(description="sigma2", value=2.3, min=0.1, max=10.0)
    rho = widgets.FloatSlider(description="rho", value=0.0, min=-0.9, max=0.9)
    r = widgets.IntSlider(description="r", value=1, min=1, max=4)
    out = widgets.interactive_output(
        PlotEj1(),
        {
            "mu1": mu1,
            "mu2": mu2,
            "sigma1": sigma1,
            "sigma2": sigma2,
            "rho": rho,
            "r": r,
        },
    )
    title = widgets.Label(
        "Seleccionar parámetros",
        layout=widgets.Layout(display="flex", justify_content="center"),
    )
    sliders = [title, mu1, mu2, sigma1, sigma2, rho, r]
    display(
        widgets.HBox(
            [out, widgets.VBox(sliders)],
            layout=widgets.Layout(width="100%", display="flex", align_items="center"),
        )
    )


if __name__ == "__main__":
    ej1()
