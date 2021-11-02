"""Ejercicio 3"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns


np.random.seed(42)


def ej3():
    """Ejercicio 3."""
    n = 2
    n_realizaciones = 1000
    sigma = 1.0
    q = 1.0
    x = np.random.normal(size=(n_realizaciones, n))
    x_bar = x.mean(axis=1)
    t = q * sigma / np.sqrt(n)
    cobertura = 100.0 * np.sum(np.abs(x_bar) <= t) / n_realizaciones
    print(f"Porcentaje de cobertura aproximada {cobertura:.0f}%")

    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    x_lims = (-3.5, 3.5)
    y_lims = (0, 0.6)
    x = np.linspace(*x_lims, n_realizaciones)
    plt.plot(
        x,
        norm.pdf(x, scale=sigma / np.sqrt(n)),
        alpha=0.9,
        c="k",
        ls="dashed",
        label="Exacta",
    )
    sns.kdeplot(x=x_bar, alpha=0.9, c="b", label="Estimación KDE")
    plt.hist(
        x=x_bar,
        rwidth=0.8,
        alpha=0.5,
        color="b",
        bins="auto",
        density=True,
        label="Histograma",
    )
    rectangulo = Rectangle(
        [-t, y_lims[0]],
        2 * t,
        y_lims[1] - y_lims[0],
        alpha=0.5,
        color="0.5",
        label=fr"Cobertura $\sim${cobertura:.0f}%",
    )
    plt.vlines(
        [-t, t],
        *y_lims,
        alpha=0.9,
        colors="0.5",
        ls="dashed",
        label=r"CL 1$\sigma$ (68%)",
    )
    sns.rugplot(x=x_bar, alpha=0.25, c="b", clip_on=False, label="Realizaciones")
    plt.gca().add_patch(rectangulo)
    plt.xlabel(r"Estimador $\bar{x}$")
    plt.ylabel("Densidad de probabilidad")
    plt.xlim(*x_lims)
    plt.ylim(y_lims[0] - 0.02, y_lims[1])
    plt.legend()
    plt.show()
    plt.close()


if __name__ == "__main__":
    ej3()
