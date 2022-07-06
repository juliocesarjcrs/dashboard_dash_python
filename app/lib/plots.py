import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from maindash import app
from components.database.conexion import categories, load_model, predict_data
from datetime import date, datetime

# print(categories.columns.unique().to_list())
options_categories = ['ALCALINAS', 'BOMBILLOS', 'ENCENDEDORES', 'MANGANESO', 'OTROS','TERCEROS'] # 'TERCEROS'
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
                     ]),
        ]),
    html.Hr(),
    dbc.Row(
        [dbc.Col(
            html.Div([html.P("Seleccione un rango de fechas que desea predecir, recuerde seleccionar únicamente el primer día del mes deseado:"),
                      dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(2021, 5, 1),
                # max_date_allowed=date(2023, 3, 1),
                # initial_visible_month=date(2022, 3, 1),
                # end_date=date(2023, 3, 25),
                # start_date=,
                display_format='MMMM YYYY',
                minimum_nights=28,
                start_date_placeholder_text='Mes Inicial',
                end_date_placeholder_text='Mes Final',
                number_of_months_shown=2

            ),
                # html.Div(id='output-container-date-picker-range'),
                html.Hr(),
                dbc.Button('Predecir', id='button-predict')

            ]),
        ),
            dbc.Col(
            dcc.RadioItems(
                id='type-frequency',
                options=[{'label': 'Mensual', 'value': 'mensual'},
                         {'label': 'Semanal', 'value': 'semanal'}],
                value='mensual'
            ),
        )
        ]),

    dbc.Col(html.P(id='error-msg')),
    dcc.Graph(id="predict-plot", config={'displayModeBar': False})
])

@callback(
    [
    Output('predict-plot', 'figure'),
     Output('error-msg', 'children')
     ],
    [Input('button-predict', 'n_clicks'),
    Input('category-predict', 'value'),
    Input('dropdown-region', 'value'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input('type-frequency', 'value')
    ],
    )
def update_output(button_val, category_value, region_select, start_date, end_date, type_freq):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if not start_date:
        return {}, 'No existe fecha de inicio'
    if not end_date:
        return {}, 'No existe fecha final'

    if 'button-predict' in changed_id:
    #print('start_date', start_date)
    #print('end_date', end_date)
        col_name = category_value+ '_'+region_select
        file_name =col_name +'.sav'
        smodel = load_model(file_name, type_freq)
        if not smodel:
            return {}, 'No se encuentra el archivo del modelo'
        f_fin = datetime.strptime(end_date, '%Y-%m-%d')
        f_ini = datetime.strptime(start_date, '%Y-%m-%d')
        num = diff_month(f_fin, f_ini)
        range_time = 'W' if type_freq =='semanal' else 'M'
        future_periods = num*4 if type_freq =='semanal' else num
        print('future_periods', future_periods, 'type range', range_time)
        predict_df = predict_data(smodel, future_periods, col_name , range_time)
        fig_result = px.line(predict_df, x='date', y="value", color="type",hover_data={"date": "|%B %d, %Y"}, title='Resultados de la predicción')
        return fig_result, ''
    else:
        return {}, ''


def diff_month(d1, d2):

    return (d1.year - d2.year) * 12 + d1.month - d2.month

