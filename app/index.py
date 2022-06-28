from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px
# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
from maindash import app
from callbacks import get_callbacks
#        APP LAYOUT:
from lib import  navbar
from pages import content


###############################################################
# Load and modify the data that will be used in the app.
#################################################################
# DATA_DIR = "data"


server = app.server


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
# def update_plot(app,df):


if __name__ == "__main__":
    app.run_server(debug=True)