import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from maindash import app
from components.database.conexion import categories


# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                   mapbox_style="carto-positron")


# cities_path = os.path.join(DATA_DIR, "worldcities.csv")
# category_path = 'app/data/df_category.csv'
# categories = pd.read_csv(category_path)
# print(categories.head())

mapa = html.Div([
    dcc.Graph(id="graph-2",config={'displayModeBar': False}),
    html.P("Names:"),
    dcc.Dropdown(id="continents-2",
        options=["Asia", "Europe", "Africa","Americas","Oceania"],
        value='Asia', clearable=False
    ),
])
@callback(
    Output("graph-2", "figure"), 
    Input("continents-2", "value"),
    )
def generate_chart_2(continents):
    df = px.data.gapminder() # replace with your own data source
    mask = df.continent == continents
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    return fig


df2 = px.data.tips() # replace with your own data source
fig2 = px.pie(df2, values='total_bill', names='day', hole=.3)

pie1 = html.Div([
    dcc.Graph(figure=fig2, id="donut")
])

df3 = px.data.tips()
fig3 = px.histogram(df3, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df3.columns)
histog = html.Div([
    dcc.Graph(figure=fig3, id="histogram")
])

df4 = px.data.stocks(indexed=True)
fig4 = px.line(df4, facet_row="company", facet_row_spacing=0.01)
linep = html.Div(
    dcc.Graph(figure=fig4, id="lineplot")
)