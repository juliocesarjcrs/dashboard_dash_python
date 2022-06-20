from dash import html
# from lib import co_map
page = html.P("This is the content of the analysis page!")

page = html.Div(
    [
        # co_map.map,
    ],
    className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
)