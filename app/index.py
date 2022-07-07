## GUI IMPORTS##
# Libraries used for interface development
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px

# Recall app
from maindash import app # Allows the program to access the same app instance from any file
from callbacks import get_callbacks # Allows the program to use the get_callbacks functions to update page visualizations
## APP LAYOUT ##
# Import app layout elements
from lib import  navbar
from pages import content

server = app.server

# App layout definition
app.layout = dbc.Container(
    [
        navbar.nav,
        html.Div([dcc.Location(id="url"), navbar.nav, content.content])
        ] # Childs 
    ) # Container
get_callbacks(app) # Calls get_callbacks function to update pages depending on web address

if __name__ == "__main__":
    app.run_server(debug=True)