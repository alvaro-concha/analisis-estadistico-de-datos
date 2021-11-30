"""Ejercicio 4"""
import numpy as np
from scipy.stats import t


def my_paired_t_test(dif):
    """Calcula test t de Student apareado sobre las diferencias"""
    bar_dif = np.mean(dif)
    s_dif = np.std(dif, ddof=1)
    n = len(dif)
    test = bar_dif / (s_dif / np.sqrt(n))
    pvalue = 1.0 - t.cdf(test, n - 1)
    return test, pvalue


def my_paired_t_test_significance_level(dif, alpha):
    """Calcula el nivel de significancia de un test t de Student apareado"""
    n = len(dif)
    return t.ppf(1.0 - alpha, n - 1)


def ej4():
    """Ejercicio 4."""
    rendimiento_horno = np.array(
        [2009, 1915, 2011, 2463, 2180, 1925, 2122, 1482, 1542, 1443, 1535]
    )
    rendimiento_aire = np.array(
        [1903, 1935, 1910, 2496, 2108, 1961, 2060, 1444, 1612, 1316, 1511]
    )
    dif = rendimiento_horno - rendimiento_aire
    alpha = 0.05

    test, pvalue = my_paired_t_test(dif)
    print(f"Student apareado: statistic {test:.2f}, p-value {pvalue * 100.0:.1f}%")
    t_c = my_paired_t_test_significance_level(dif, alpha)
    print(f"\t\t  valor crítico {t_c:.2f}, alpha {alpha * 100.0:.1f}%")

    bar_horno = np.mean(rendimiento_horno)
    bar_aire = np.mean(rendimiento_aire)
    print(f"Promedio: horno {bar_horno:.0f}, aire {bar_aire:.0f}")

    s_horno = np.std(rendimiento_horno, ddof=1)
    s_aire = np.std(rendimiento_aire, ddof=1)
    print(f"Desviación: horno {s_horno:.0f}, aire {s_aire:.0f}")


if __name__ == "__main__":
    ej4()
