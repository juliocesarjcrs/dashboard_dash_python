# Basics Requirements
import pathlib
import os
from dash import Dash,html,Input, Output, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px
# Dash Bootstrap Components
import dash_bootstrap_components as dbc
# Data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json
# Recall app
from app import app
from callbacks import get_callbacks
###########################################################
#        APP LAYOUT:
###########################################################

# LOAD THE DIFFERENT FILES
from lib import title, navbar
from pages import content, analysis, prediction, train, not_found

# app.layout = html.Div(
#     [   # title.main_title,
#         navbar.nav,
#         content.content
#         # sidebar.sidebar,
#     ],
#     className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
# )


###############################################
#           APP INTERACTIVITY:
###############################################
# app.layout = html.Div([dcc.Location(id="url"), navbar.nav, content.content])


###############################################################
# Load and modify the data that will be used in the app.
#################################################################
# DATA_DIR = "data"


# server = app.server

app = Dash(__name__)
app.title = 'Inicio'
app.layout = dbc.Container([
    html.H1(['Inicio']),
    navbar.nav,
    html.Div([dcc.Location(id="url"), navbar.nav, content.content])

]
)
get_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
