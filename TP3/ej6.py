"""Ejercicio 6"""
import numpy as np
import plotly.graph_objects as go


def ej6():
    """Ejercicio 6."""
    x = np.array(
        [
            1,
            2.5,
            3.1,
            4,
            5.5,
        ]
    )
    X = np.column_stack([np.ones_like(x), x])
    mu_y = np.array(
        [
            1.85,
            2.72,
            5.15,
            5.7,
            6.9,
        ]
    )
    sigma_y = 0.5
    Sigma_y = np.eye(len(mu_y)) * sigma_y ** 2
    B = np.array(
        [[0.834, 0.406, 0.234, -0.023, -0.451], [-0.197, -0.064, -0.011, 0.069, 0.202]]
    )
    mu_theta = B @ mu_y
    mu_y0 = mu_theta[0]
    mu_m = mu_theta[1]
    Sigma_theta = B @ Sigma_y @ B.T
    sigma_y0 = np.sqrt(Sigma_theta[0, 0])
    sigma_m = np.sqrt(Sigma_theta[1, 1])
    rho_theta = Sigma_theta[0, 1] / (sigma_y0 * sigma_m)
    print(f"mu_y0\t\t{mu_y0:.2f}")
    print(f"sigma_y0\t{sigma_y0:.2f}")
    print(f"mu_m\t\t{mu_m:.2f}")
    print(f"sigma_m\t\t{sigma_m:.2f}")
    print(f"rho_theta\t{rho_theta:.2f}")
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=mu_y,
            error_y_array=np.full_like(mu_y, sigma_y),
            mode="markers",
            name="Datos",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=x,
            y=X @ mu_theta,
            mode="lines",
            name="Ajuste",
        )
    )
    fig.update_traces(opacity=0.75)
    fig.update_layout(
        xaxis_title_text="x",
        yaxis_title_text="y",
    )
    fig.show(renderer="notebook")


if __name__ == "__main__":
    ej6()
