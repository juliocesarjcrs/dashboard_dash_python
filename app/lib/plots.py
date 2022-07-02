import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from maindash import app
from components.database.conexion import categories, forecast_plot
from datetime import date
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                   mapbox_style="carto-positron")


# print(categories.columns.unique().to_list())
options_categories = ['ALCALINAS', 'BOMBILLOS', 'ENCENDEDORES', 'MANGANESO', 'OTROS', 'TERCEROS']

#
mapa = html.Div([
    html.P("Seleccione una categoría:"),
    dcc.Dropdown(id="category",
        options=options_categories,
        value='ALCALINAS', clearable=False
    ),
    dcc.Dropdown(id="dates",
        options=['month', 'year', 'year_month','date'],
        value='month', clearable=False
    ),
    dcc.Graph(id="graph",config={'displayModeBar': False}),
])
@callback(
    Output("graph", "figure"), 
    Input("category", "value"),
    Input("dates","value")
    )
def generate_chart(cat,dates):
    if dates == 'date':
        fig = px.line(categories, x=categories[dates], y=categories[cat])
    else:
        datos = categories.groupby([dates]).sum().reset_index()
        # print(datos[cat])
        fig = px.line(categories, x=datos[dates], y=datos[cat])
    
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




fig5 = px.line(forecast_plot, x='date', y="value", color="type",hover_data={"date": "|%B %d, %Y"}, title='Resultados de la predicción')
# fig_predict = html.Div(
#     dcc.Graph(figure=fig5, id="lineplot-2")
# )

fig_predict = html.Div([
    dbc.Row(
        [
            dbc.Col([
                html.P("Seleccione una categoría:"),
                dcc.Dropdown(id="category-predict",
                             options=options_categories,
                             value='ALCALINAS', clearable=False
                             )]),
            dbc.Col([html.P("Seleccione una región:"),
                     dcc.Dropdown(id="region",
                                  options=['BOGOTÁ', 'CENTRO',
                                           'NORTE', 'SANTANDER', 'SUR'],
                                  value='BOGOTÁ', clearable=False
                                  )
                     ])
        ]),
    dbc.Row(
        [dbc.Col(
            html.Div([html.P("Seleccione rango de fechas:"),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=date(1995, 8, 5),
                    max_date_allowed=date(2017, 9, 19),
                    initial_visible_month=date(2017, 8, 5),
                    end_date=date(2017, 8, 25)
                ),
                html.Div(id='output-container-date-picker-range')
            ])
        )

        ]),
    dcc.Graph(figure=fig5, id="predict-plot",
              config={'displayModeBar': False}),
])


