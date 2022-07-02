from dash import html, dcc
import dash_bootstrap_components as dbc
page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/run-line2.png'),width=1),
            dbc.Col(html.H3('Entrenamiento'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container([
            html.P('Arrastre el conjunto de datos que desea procesar:'),
            html.Div([
                dcc.Upload([
                    'Arrastre y suelte o ',
                    html.A('Seleccione un archivo')
                ], style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center'
                })
            ])]
        )])