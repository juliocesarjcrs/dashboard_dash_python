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
#        APP LAYOUT:
from lib import title, navbar
from pages import content, analysis, prediction, train, not_found


###############################################################
# Load and modify the data that will be used in the app.
#################################################################
# DATA_DIR = "data"


# server = app.server

app = Dash(__name__) # Relate app with this file specifically
app.title = 'Inicio' # Tab title
# App layout definition
app.layout = dbc.Container(
    [
        html.H1(['Inicio']),
        navbar.nav,
        html.Div([dcc.Location(id="url"), navbar.nav, content.content])
        ] # Childs 
    ) # Container
get_callbacks(app) # Calls get_callbacks function to update pages depending on web address

if __name__ == "__main__":
    app.run_server(debug=True)