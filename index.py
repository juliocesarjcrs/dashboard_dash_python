# Basics Requirements
import pathlib
import os
from dash import html,Input, Output, dcc
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

###########################################################
#
#           APP LAYOUT:
#
###########################################################


# LOAD THE DIFFERENT FILES
from lib import title, sidebar, navbar
from pages import content, analysis, prediction, train, not_found

app.layout = html.Div(
    [
        # title.main_title,
        navbar.nav,
        content.content

        # sidebar.sidebar,
    ],
    className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
)


###############################################
#
#           APP INTERACTIVITY:
#
###############################################

app.layout = html.Div([dcc.Location(id="url"), navbar.nav, content.content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    print(pathname)
    if pathname == "/":
        return analysis.page
    elif pathname == "/prediction":
        return prediction.page
    elif pathname == "/train":
        return train.page
    # If the user tries to reach a different page, return a 404 message
    return not_found.page
###############################################################
# Load and modify the data that will be used in the app.
#################################################################
DATA_DIR = "data"
cities_path = os.path.join(DATA_DIR, "worldcities.csv")
world_cities = pd.read_csv(cities_path)
cities = world_cities[world_cities['iso2'] == 'CO']
print(cities.head(2))



if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port="8050", debug=True)
