"""Ejercicio 5"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns


def ej5():
    """Ejercicio 5."""
    mu_0 = 110.6
    sigma_0 = 24.8
    mu_1 = 142.3
    sigma_1 = 29.6
    x_lims = (0, 250)
    x = np.linspace(*x_lims, 10000)
    f_0 = norm(loc=mu_0, scale=sigma_0).pdf
    f_1 = norm(loc=mu_1, scale=sigma_1).pdf
    phi = norm.cdf
    x_c = (sigma_1 * mu_0 + sigma_0 * mu_1) / (sigma_0 + sigma_1)
    alpha_c = phi((mu_0 - x_c) / sigma_0)
    beta_c = phi((x_c - mu_1) / sigma_1)
    precision_c = 1 - alpha_c
    x_OMS = 126.0
    alpha_OMS = phi((mu_0 - x_OMS) / sigma_0)
    beta_OMS = phi((x_OMS - mu_1) / sigma_1)
    cociente_OMS = alpha_OMS / beta_OMS
    dif_rel_OMS = np.abs(alpha_OMS - beta_OMS) / (0.5 * (alpha_OMS + beta_OMS))
    precision_OMS = 1 - alpha_OMS
    prior = 0.35
    likelihood = 1 - beta_OMS
    marginal = alpha_OMS * (1 - prior) + (1 - beta_OMS) * prior
    posterior = likelihood * prior / marginal

    print(f"Valor critico:\tx_c = {x_c:.2f} mg/dl")
    print(f"Error tipo I:\talpha_c = {alpha_c:.2f}")
    print(f"Error tipo II:\tbeta_c = {beta_c:.2f}")
    print(f"Precision:\tPrecision_c = {precision_c:.2f}")
    print()
    print(f"Valor OMS:\tx_OMS = {x_OMS:.2f} mg/dl")
    print(f"Error tipo I:\talpha_OMS = {alpha_OMS:.2f}")
    print(f"Error tipo II:\tbeta_OMS = {beta_OMS:.2f}")
    print(f"Cociente:\talpha_OMS / beta_OMS = {cociente_OMS:.2f}")
    print(f"Dif. relativa:\t{dif_rel_OMS:.2f}")
    print(f"Precision:\tPrecision_OMS = {precision_OMS:.2f}")
    print(f"Posterior:\t{posterior:.2f}")

    plt.figure(figsize=(8, 8))
    sns.set_context("paper", font_scale=1.5)
    plt.plot(x, f_0(x), label=r"$f_0$")
    plt.plot(x, f_1(x), label=r"$f_1$")
    y_lims = plt.gca().get_ylim()
    plt.vlines(x_c, *y_lims, ls="-", colors="k", label=r"$x_c$")
    plt.vlines(x_OMS, *y_lims, ls="--", colors="k", label=r"$x_{\mathrm{OMS}}$")
    plt.legend()
    plt.title("Umbral de decisión")
    plt.xlabel(r"$x$")
    plt.ylabel(r"Densidad de probabilidad")
    plt.savefig("tp6_ej5.pdf", bbox_inches="tight")
    plt.show()
    plt.close()


if __name__ == "__main__":
    ej5()
