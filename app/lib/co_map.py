import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
import numpy as np

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os

# DATA_DIR = "data"
# cities_path = os.path.join(DATA_DIR, "worldcities.csv")
# world_cities = pd.read_csv(cities_path)
# cities = world_cities[world_cities['iso2'] == 'CO']
# cities['magnitude'] = np.random.randint(1, 300, cities.shape[0])
cities = pd.DataFrame()

d = {'lat': [1, 2], 'lng': [3, 4], 'magnitude': [1, 0]}
cities = pd.DataFrame(data=d)

Map_Fig = px.density_mapbox(cities, lat='lat', lon='lng', z='magnitude', radius=10,
                        center=dict(lat=4.570868, lon=-74.297333),
                        zoom=3, #zoom (int (default 8)) – Between 0 and 20. Sets map zoom level.
                        mapbox_style="stamen-terrain")
Map_Fig.update_layout(title="COL map", paper_bgcolor="#F8F9F9")


##############################
# Map Layout
##############################
map = html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=Map_Fig, id="US_map")
    ],
    className="ds4a-body",
)