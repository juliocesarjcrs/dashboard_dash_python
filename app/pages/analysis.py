from dash import html
from lib import plots
import dash_bootstrap_components as dbc

page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/bar-chart-2-line.png'),width=1),
            dbc.Col(html.H3('Análisis'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container([
            dbc.Row([
                html.P('A continuación encontrará el comportamiento de las unidades vendidas por categoría en distintos intervalos de tiempo.'),
                plots.mapa,
                ]),
            # dbc.Row([
            #     html.P('Aquí Se mostraría la distribución de otras variables de interés, como las referencias más vendidas o comparaciones anuales'),
            #     dbc.Col(plots.pie1),
            #     dbc.Col(plots.histog)
            #     ])
        ])

    ])