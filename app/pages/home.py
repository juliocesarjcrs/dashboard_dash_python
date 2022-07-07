from dash import html
from lib import plots
import dash_bootstrap_components as dbc
page = dbc.Container([
        ## Page Header ##
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/home-6-fill.png'),width=1),
            dbc.Col(html.H3('Bienvenido'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container([
            html.P('A continuación encontrará una descripción general de cada una de las pestañas:'),
            html.H4('Análisis:'),
            html.P('En esta ventana podrá visualizar los datos históricos de unidades vendidas por categoría y región en periodos de tiempo diarios, semanales y mensuales'),
            html.H4('Predicción:'),
            html.P('Esta ventana le permite seleccionar un periodo de tiempo de mínimo 3 meses a partir del cual el modelo mostrará una predicción de las unidades que podrían venderse'),
            html.H4('Entrenamiento:'),
            html.P('Aquí podrá arrastrar y cargar nuevos modelos que desee implementar'),
            ])

    ])