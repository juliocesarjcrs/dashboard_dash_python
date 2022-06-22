import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}
nav = html.Div(
    [
        html.H1("Tronex"),
        html.Hr(),
        html.P(
            "Seleccione la pantalla de interés:"),
        dbc.Nav(
            [
                dbc.NavLink("Bienvenida", href="/", active="exact"),
                dbc.NavLink("Análisis", href="/analisis", active="exact"),
                dbc.NavLink("Predicción", href="/prediction", active="exact"),
                dbc.NavLink("Entrenamiento", href="/train", active="exact"),
                dbc.NavLink("Configuración",href="/config",active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
