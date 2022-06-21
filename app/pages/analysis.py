from dash import html
from lib import plots
import dash_bootstrap_components as dbc
# from lib import co_map
# page = html.P("This is the content of the analysis page!")

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
                html.P('Aquí puede ir un mapa con la distribución de los clientes y la cantidad de productos por región'),
                plots.mapa,
                ]),
            dbc.Row([
                html.P('Aquí Se mostraría la distribución de otras variables de interés, como las referencias más vendidas o comparaciones anuales'),
                dbc.Col(plots.pie1),
                dbc.Col(plots.histog)
                ])
        ])

    ])