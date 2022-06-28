# # Basics Requirements
# from dash import Dash,html,Input, Output, dcc
# import dash_bootstrap_components as dbc
# from dash.exceptions import PreventUpdate
# import plotly.graph_objects as go
# import plotly.express as px
# # Dash Bootstrap Components
# import dash_bootstrap_components as dbc
# # Data
# import math
# import numpy as np
# import datetime as dt
# import pandas as pd
# import json
# # Recall app
# from maindash import app
# from callbacks import get_callbacks
# #        APP LAYOUT:
# from lib import  navbar
# from pages import content, analysis, prediction, train, not_found


# ###############################################################
# # Load and modify the data that will be used in the app.
# #################################################################
# # DATA_DIR = "data"

# print('1-entra index')
# server = app.server
# print('2-entra index')

# app.title = 'Inicio' # Tab title
# # App layout definition
# app.layout = dbc.Container(
#     [
#         html.H1(['Inicio']),
#         navbar.nav,
#         html.Div([dcc.Location(id="url"), navbar.nav, content.content])
#         ] # Childs 
#     ) # Container
# get_callbacks(app) # Calls get_callbacks function to update pages depending on web address
# # def update_plot(app,df):
# print('3-entra index')

# if __name__ == "__main__":
#     app.run_server(debug=True)
from dash import Dash, dcc, html, Input, Output
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA', 'NYC', 'MTL'],
        'LA',
        id='dropdown'
    ),
    html.Div(id='display-value')
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)