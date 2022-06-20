from dash import html
import dash_bootstrap_components as dbc
page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/run-line.png'),width=1),
            dbc.Col(html.H3('Entrenamiento'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container(
            html.P('Aquí van las gráficas')
        )

    ])