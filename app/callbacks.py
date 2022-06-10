from dash import Input, Output
from pages import content, analysis, prediction, train, not_found
def get_callbacks(app):
    @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def render_page_content(pathname):
        if pathname == "/":
            return analysis.page
        elif pathname == "/prediction":
            return prediction.page
        elif pathname == "/train":
            return train.page
        # If the user tries to reach a different page, return a 404 message
        return not_found.page