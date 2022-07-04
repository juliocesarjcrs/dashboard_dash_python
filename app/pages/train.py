from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import base64
# import datetime
import io
import pandas as pd

page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/run-line2.png'),width=1),
            dbc.Col(html.H3('Entrenamiento'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container([
            html.P('Arrastre el conjunto de modelos que desea agregar:'),
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
            ]),
            html.Div(id='out-datatable')
            ]
        )])
@callback(
    Output("out-datatable", "children"), 
    Input("up-data", "content"),
    Input("up-data", "filename"),
    Input("up-data", "last-modified"),
    )
def generate_table(list_content,list_names,list_dates):
    if list_content is not None:
        children = [

        ]
def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])