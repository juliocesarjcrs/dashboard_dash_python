import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from maindash import app
from components.database.conexion import categories, forecast_plot, load_model, predict_data
from datetime import date
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
#                   color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
#                   mapbox_style="carto-positron")


# print(categories.columns.unique().to_list())
options_categories = ['ALCALINAS', 'BOMBILLOS', 'ENCENDEDORES', 'MANGANESO', 'OTROS'] # 'TERCEROS'
regiones = ['BOGOTÁ', 'CENTRO','NORTE', 'SANTANDER', 'SUR']


#
mapa = html.Div([
    html.P("Seleccione una categoría:"),
    dcc.Dropdown(id="category",
        options=options_categories,
        value='ALCALINAS', clearable=False
    ),
    html.P("Seleccione un periodo:"),
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
        fig = px.line(categories, x=dates, y=cat)
    else:
        datos = categories.groupby([dates]).sum().reset_index()
        # print(datos[cat])
        fig = px.line(datos, x=dates, y=cat)
    
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
                     dcc.Dropdown(id="dropdown-region",
                                  options=regiones,
                                  value='BOGOTÁ', clearable=False
                                  )
                     ])
        ]),
    dbc.Row(
        [dbc.Col(
            html.Div([html.P("Seleccione rango de fechas:"),
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=date(2022, 3, 1),
                    max_date_allowed=date(2023, 3, 1),
                    initial_visible_month=date(2022, 3, 1),
                    end_date=date(2022, 3, 25),
                    start_date=date(2023, 4, 25),
                    display_format='MMM YYYY'
                ),
                html.Div(id='output-container-date-picker-range')
            ])
        ),
        dbc.Col( html.Button('Predecir', id='button-predict'),)

        ]),
    dcc.Graph( id="predict-plot",config={'displayModeBar': False})
])

@callback(
    Output('predict-plot', 'figure'),
    [Input('button-predict', 'n_clicks'),
    Input('category-predict', 'value'),
    Input('dropdown-region', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date')
    ],
    )
def update_output(n_clicks, category_value, region_select, start_date, end_date):
    if n_clicks is None:
        fig5 = px.line(forecast_plot, x='date', y="value", color="type",hover_data={"date": "|%B %d, %Y"}, title='Resultados de la predicción')
        return fig5
    #print('start_date', start_date)
    #print('end_date', end_date)
    file_name =category_value+ '_'+region_select+'.sav'
    smodel = load_model(file_name)
    fitted_series = predict_data(smodel, 3, 'M')
    #print(fitted_series)
    forecast = pd.DataFrame(fitted_series, index = fitted_series.index, columns=['value'])
    forecast_load = forecast.reset_index()
    predict_df = forecast_load
    predict_df['type'] = 'predict'
    print(predict_df.head(3))

    fig_result = px.line(predict_df, x='index', y="value", color="type",hover_data={"index": "|%B %d, %Y"}, title='Resultados de la predicción')
    return fig_result


