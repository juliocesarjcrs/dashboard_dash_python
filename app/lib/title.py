# Basics Requirements
import pathlib
from dash import  html

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from app import app

main_title = html.Div(
    className="ds4a-title",
    children=[
        dbc.Row(dbc.Col(html.H1("Tronex Dashboard"), width={"size": 6, "offset": 3}))
    ],
    id="title",
)
