## Dash Imports ##
from dash import html
import dash_bootstrap_components as dbc
## Other functionalities ##
from lib import plots

page = dbc.Container([
        ## Page Header ##
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/bar-chart-2-line.png'),width=1),
            dbc.Col(html.H3('Análisis'),width=1),
            html.Hr()
        ]
        ),
        ## Plot Container ##
        dbc.Container([
            dbc.Row([
                plots.fig_analysis,
                ]),
            ## ADD ADDITIONAL PLOTS HERE ##

            # dbc.Row([
            #     html.P('HERE YOU CAN ADD ADDITIONAL INFORMATION FOR THE NEW PLOTS'),
            #     dbc.Col(plots.pie1), # PIE PLOT EXAMPLE
            #     dbc.Col(plots.histog) # HISTOGRAM PLOT EXAMPLE
            #     ])
        ])

    ])