## Dash Imports ##
from dash import Dash, html, dcc, Input, Output, callback, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px

## Other functionalities ##
import pandas as pd
from datetime import date, datetime
import numpy as np

## App Recalls ##
from maindash import app # This enable the access to the main app instance from this file if needed
from components.database.conexion import last_date_train, df_category_regional, load_model, predict_data # Load datasets

# Create dropdowns' lists
options_categories = ['ALCALINAS', 'BOMBILLOS', 'ENCENDEDORES', 'MANGANESO', 'OTROS','TERCEROS'] # 'TERCEROS'
regiones = ['BOGOTÁ', 'CENTRO','NORTE', 'SANTANDER', 'SUR']

#########################
## Analysis Page Plots ##
#########################

fig_analysis = html.Div([
    html.P('A continuación encontrará el comportamiento de las unidades vendidas por categoría en distintos intervalos de tiempo.'),
    dbc.Row([
        dbc.Col([
            ## Category dropdown ##
            html.P("Seleccione una categoría:"),
            dcc.Dropdown(id="category",
                options=options_categories,
                value='ALCALINAS', clearable=False
            )
        ]),
        dbc.Col([
            ## Date period dropdown ##
            html.P("Seleccione un periodo:"),
            dcc.Dropdown(id="dates",
                options = [{'label': 'Mensual', 'value': 'year_month'},
                            {'label': 'Semanal', 'value': 'year_week'},
                            {'label' :'Diario', 'value':'date'}],
                # options=['year_month','year_week','date'],
                value='year_month', clearable=False
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            ## Region dropdown ##
            html.P("Seleccione una región:"),
            dcc.Dropdown(id="region",
                options=regiones,
                value='BOGOTÁ', clearable=False
            )
        ]),
    ]),
    dcc.Graph(id="graph",config={'displayModeBar': False}),
])

@callback(
    Output("graph", "figure"), 
    Input("category", "value"),
    Input("dates","value"),
    Input("region","value")
    )
## This callback updates the lineplot based on the category, date and region dropdowns values ##
def generate_chart(cat,dates,region):
    sel = cat+'_'+region
    df_ = df_category_regional.groupby([dates])[sel].sum().reset_index() # Grouping data
    if dates == 'date':
        # Daily plot
        fig = px.line(data_frame = df_, x = dates, y = sel)
    else:
        # Weekly and monthly plot
        fig = px.line(data_frame = df_, x = dates, y = sel)
        step = 10
        x = list(np.arange(1,len(df_),step))
        fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = x,
            ticktext = list(df_[dates][x].values),
            tickangle = 90
            )
            )
    return fig

## PIE PLOT EXAMPLE ##
df2 = px.data.tips() # Replace with your own data source
fig2 = px.pie(df2, values='total_bill', names='day', hole=.3)

pie1 = html.Div([
    dcc.Graph(figure=fig2, id="donut")
])

## HISTOGRAM PLOT EXAMPLE ##
df3 = px.data.tips() # Replace with your own data source
fig3 = px.histogram(df3, x="total_bill", y="tip", color="sex", marginal="rug", hover_data=df3.columns)
histog = html.Div([
    dcc.Graph(figure=fig3, id="histogram")
])

###########################
## Prediction Page Plots ##
###########################

fig_predict = html.Div([
    dbc.Row(
        [
            dbc.Col([
                ## Category dropdown ##
                html.P("Seleccione una categoría:"),
                dcc.Dropdown(id="category-predict",
                             options=options_categories,
                             value='ALCALINAS', clearable=False
                             )]),
            dbc.Col([
                ## Region dropdown ##
                html.P("Seleccione una región:"),
                dcc.Dropdown(id="dropdown-region",
                            options=regiones,
                            value='BOGOTÁ', clearable=False
                            )]),
        ]),
    html.Hr(),
    dbc.Row(
        ## Predicion Date Picker ##
        [dbc.Col(
            html.Div([html.P("Seleccione un rango de fechas que desea predecir, recuerde seleccionar únicamente el primer día del mes deseado:"),
                      dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=date(last_date_train['year'], last_date_train['month'], last_date_train['day']),
                # max_date_allowed=date(2023, 3, 1),
                initial_visible_month=date(last_date_train['year'], last_date_train['month'], last_date_train['day']),
                # end_date=date(2023, 3, 25),
                start_date=date(last_date_train['year'], last_date_train['month'], last_date_train['day']),
                display_format='MMMM YYYY',
                minimum_nights=90,
                start_date_placeholder_text='Mes Inicial',
                end_date_placeholder_text='Mes Final',
                number_of_months_shown=2

            ),
                html.Hr(),
                dbc.Button('Predecir', id='button-predict')

            ]),
        ),
        dbc.Col([
            ## Period Selector (Weekly or Monthly) ##
            html.P("Seleccione el tipo de periodos que desea predecir:"),
                dcc.RadioItems(
                    id='type-frequency',
                    options=[{'label': 'Mensual', 'value': 'mensual'},
                            {'label': 'Semanal', 'value': 'semanal'}],
                    value='mensual',
                    labelStyle={'display': 'block', 'padding-bottom': '10px', 'padding-top': '10px'}
                ),
        ]),
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
## This callback updates the prediction plot after checking input mistakes that could be made by the user ##
def update_output(button_val, category_value, region_select, start_date, end_date, type_freq):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if not start_date:
        return {}, 'No existe fecha de inicio'
    if not end_date:
        return {}, 'No existe fecha final'

    if 'button-predict' in changed_id:
        col_name = category_value+ '_'+region_select
        file_name =col_name +'.sav'
        smodel = load_model(file_name, type_freq)
        if not smodel:
            return {}, 'No se encuentra el archivo del modelo'
        f_fin = datetime.strptime(end_date, '%Y-%m-%d')
        f_ini = datetime.strptime(start_date, '%Y-%m-%d')
        num = diff_month(f_fin, f_ini)
        range_time = 'W' if type_freq =='semanal' else 'M'
        future_periods = num*10*4 if type_freq =='semanal' else num *10
        print('future_periods', future_periods, 'type range', range_time)
        predict_df = predict_data(smodel, future_periods, col_name , range_time)
        fig_result = px.line(predict_df, x='date', y="value", color="type",hover_data={"date": "|%B %d, %Y"}, title='Resultados de la predicción')
        return fig_result, ''
    else:
        return {}, ''

## Function to calculate month between selected dates on the date picker ##
def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

