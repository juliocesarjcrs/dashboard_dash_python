from dash import html
from lib import plots
import dash_bootstrap_components as dbc
page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/home-6-fill.png'),width=1),
            dbc.Col(html.H3('Bienvenido'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container([
            html.P('A continuación encontrará las instrucciones básicas para implementar esta herramienta:'),
            ])

    ])