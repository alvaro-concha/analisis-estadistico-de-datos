"""Ejercicio 6: Ayuda a Fermat

La solución de Fermat al problema de la división justa de la bolsa es impráctica cuando quedan muchas rondas por jugar ya que implica contar todas las partidas que dan por ganador a uno de los dos jugadores.

Afortunadamente con simulaciones Monte Carlo es posible encontrar una solución aproximada.

Supongamos que un juego de 51 rondas es interrumpido en la ronda 25 y que Fermat ganó 15 rondas y Pascal 10.

Simular el resto de las rondas para decidir cuál jugador gana la partida.

Repetir este procedimiento 1000 veces para encontrar la división justa de la bolsa.
"""
import numpy as np
import pandas as pd
from scipy.special import comb

np.random.seed(42)


class DivisionJusta:
    """Simulacion del problema de division justa de la bolsa en una partida interrumpida."""

    def __init__(self, n_rondas=51, n_inter=25, F_win_inter=15, P_win_inter=10):
        self.n_rondas = n_rondas
        self.n_inter = n_inter
        self.F_win = F_win_inter
        self.P_win = P_win_inter

    def __call__(self):
        coin_toss = np.random.choice([0, 1], size=self.n_rondas - self.n_inter)
        self.F_win += np.sum(coin_toss == 1)
        self.P_win += np.sum(coin_toss == 0)
        return {
            "F_win": self.F_win,
            "P_win": self.P_win,
            "Division": self.F_win > self.P_win,
        }


def resultado_exacto(n_rondas=51, n_inter=25, F_win_inter=15, P_win_inter=10):
    """Division justa exacta, surge de contar todas las realizaciones posibles usando el triangulo de Pascal."""
    n_rest = n_rondas - n_inter
    r = n_rondas // 2 + 1 - F_win_inter
    s = n_rondas // 2 + 1 - P_win_inter
    division = 0
    for k in range(s):
        division += comb(r + s - 1, k)
    division /= 2 ** n_rest
    return division


def ej6():
    """Ejercicio 6."""
    n_ensemble = 1000
    resultados = []
    for _ in range(n_ensemble):
        juego = DivisionJusta()
        resultados.append(juego())
    resultados = pd.DataFrame(resultados)
    print("Variables Promedios\n", resultados.mean(axis=0))
    print("Resultado exacto\n", f"Division {resultado_exacto():.3f}")


if __name__ == "__main__":
    ej6()
