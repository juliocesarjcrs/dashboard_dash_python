## Dash Imports ##
from dash import html
import dash_bootstrap_components as dbc

## THIS IS AN ADDITIONAL PAGE YOU CAN USE TO ADD A NEW PAGE TO THE MENU
## YOU JUST HAVE TO UNCOMMENT LINE 24 ON 'navbar.py' AND THE BUTTON WILL
## APPEAR ON THE MENU AND THE PAGE WILL RENDER

page = dbc.Container([
        dbc.Row(
        [
            dbc.Col(html.Img(src='assets/settings-line.png'),width=1),
            dbc.Col(html.H3('New Page'),width=1),
            html.Hr()
        ]
        ),
        dbc.Container(
            html.P('Add content here')
        )

    ])