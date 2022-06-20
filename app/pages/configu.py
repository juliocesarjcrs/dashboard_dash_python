from dash import html
import dash_bootstrap_components as dbc
# from lib import co_map
# page = html.P("This is the content of the analysis page!")

page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/settings-line.png'),width=1),
            dbc.Col(html.H3('Configuración'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container(
            html.P('Aquí van las gráficas')
        )

    ])