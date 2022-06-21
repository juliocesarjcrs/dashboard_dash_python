
from dash import Input, Output
from pages import configu, analysis, prediction, train, not_found
def get_callbacks(app):
    # Callback method call
    @app.callback(
        Output(component_id="page-content", component_property="children"), # Components that recieve the output
        [Input(component_id="url", component_property="pathname")] # Components from where I get the input
        )
    def render_page_content(pathname):
        if pathname == "/":
            return analysis.page
        elif pathname == "/prediction":
            return prediction.page
        elif pathname == "/train":
            return train.page
        elif pathname == "/config":
            return configu.page
        # If the user tries to reach a different page, return a 404 message
        return not_found.page