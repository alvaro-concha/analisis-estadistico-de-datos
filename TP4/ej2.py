"""Ejercicio 2"""
import numpy as np
import plotly.graph_objects as go
from plotly.graph_objs.layout import XAxis


def ej2():
    """Ejercicio 2."""
    r = np.arange(0, 4.1, 0.1)
    acum_r = (1 - np.exp(-0.5 * r ** 2)) * 100.0
    q = np.arange(0, 16.5, 0.5)
    acum_q = (1 - np.exp(-0.5 * q)) * 100.0
    layout = go.Layout(
        xaxis=XAxis(
            title="r",
            titlefont_color="blue",
            tickfont_color="blue",
        ),
        xaxis2=XAxis(
            title="q",
            overlaying="x",
            side="top",
            titlefont_color="red",
            tickfont_color="red",
        ),
        yaxis_title="Probabilidad acumulada (%)",
    )
    fig = go.Figure(layout=layout)
    fig.add_trace(
        go.Scatter(x=q, y=acum_q, name="Acumulada q", line_color="red", xaxis="x2")
    )
    fig.add_trace(
        go.Scatter(x=r, y=acum_r, name="Acumulada r", line_color="blue", xaxis="x1")
    )
    fig.update_traces(opacity=0.9)
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej2()
