from dash import html
from lib import plots
import dash_bootstrap_components as dbc
page = dbc.Container([
        ## Page Header ##
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/focus-2-line.png'),width=1),
            dbc.Col(html.H3('Predicción'),width=1),
            html.Hr()
        ]
        ),
        ## Plot Container ##
        dbc.Container([
            html.P('Aquí va la gráfica central con las predicciones del modelo'),
            dbc.Container([
                plots.fig_predict
            ])
            ])

    ])