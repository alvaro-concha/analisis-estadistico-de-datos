"""Ejercicio 2"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ej2():
    """Ejercicio 2."""
    sigma = 1.8
    q = 1.0
    x = np.array([16.2, 12.4, 19.4, 17.3, 16.8, 24.4, 10.7, 18.1, 14.2, 14.8])
    n = len(x)
    x_bar = x.mean()
    print(
        f"Intervalo CL 1 sigma para la media: {x_bar:.1f} +- {q*sigma/np.sqrt(n):.1f}"
    )

    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    x_lims = (15, 18)
    mu = np.linspace(*x_lims, 1000)
    expected_value = mu
    upper_bound = mu + q * sigma / np.sqrt(n)
    lower_bound = mu - q * sigma / np.sqrt(n)
    plt.plot(mu, expected_value, c="k", label=r"E$(\bar{x})=\mu$")
    plt.plot(
        mu, upper_bound, c="r", label=r"$\bar{x}_2 = \mu + q\frac{\sigma}{\sqrt{n}}$"
    )
    plt.plot(
        mu, lower_bound, c="b", label=r"$\bar{x}_1 = \mu - q\frac{\sigma}{\sqrt{n}}$"
    )
    plt.hlines(
        x_bar, x_lims[0], x_bar + q * sigma / np.sqrt(n), colors="k", ls="dashed"
    )
    plt.plot(
        [x_bar - q * sigma / np.sqrt(n)] * 2,
        [x_lims[0] - q * sigma / np.sqrt(n), x_bar],
        c="r",
        ls="dashed",
        label=r"$t_1 = \bar{x} - q\frac{\sigma}{\sqrt{n}}$",
    )
    plt.plot(
        [x_bar + q * sigma / np.sqrt(n)] * 2,
        [x_lims[0] - q * sigma / np.sqrt(n), x_bar],
        c="b",
        ls="dashed",
        label=r"$t_2 = \bar{x} + q\frac{\sigma}{\sqrt{n}}$",
    )
    plt.title("Cinturón de confianza")
    plt.xlabel(r"Parámtero $\mu$")
    plt.ylabel(r"Estimador $\bar{x}$")
    plt.legend()
    plt.show()
    plt.close()


if __name__ == "__main__":
    ej2()
