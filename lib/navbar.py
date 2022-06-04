import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
# nav = dbc.Nav(
#     [
#         dbc.NavItem(dbc.NavLink("Analisis", active=True, href="#")),
#         dbc.NavItem(dbc.NavLink("Predicción", href="#")),
#         dbc.NavItem(dbc.NavLink("Entrenamiento", href="#")),
#         dbc.NavItem(dbc.NavLink("Ajustes", disabled=True, href="#")),
#     ],
#     vertical="md",
# )
# the style arguments for the sidebar. We use position:fixed and a fixed width
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
        html.H2("Tronex", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Análisis", href="/", active="exact"),
                dbc.NavLink("Predicción", href="/prediction", active="exact"),
                dbc.NavLink("Entrenamiento", href="/train", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
