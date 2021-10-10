"""Ejercicio 4"""


def ej4():
    """Ejercicio 4."""
    mu_p = 0.28
    sigma_p = 0.05

    def VE(p):
        return (1 - 2 * p) / (1 - p)

    def sigma_VE(p, sigma):
        return 1 / ((1 - p) ** 2) * sigma

    print(f"E(VE)\t\t{VE(mu_p):.2f}")
    print(f"sigma(VE)\t{sigma_VE(mu_p, sigma_p):.2f}")


if __name__ == "__main__":
    ej4()
