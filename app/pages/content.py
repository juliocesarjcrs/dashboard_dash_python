## Dash Imports ##
from dash import html

## Content styler for space between html elements on the page ##
CONTENT_STYLE = {
    "marginLeft": "15rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}
content = html.Div(id="page-content", style=CONTENT_STYLE)