## MAIN APP INSTANCE ##
import dash_auth
from dash import Dash

from decouple import config
# Get environment variables
USER_APP = config('USER_APP')
PASSWORD_APP = config('PASSWORD_APP')

VALID_USERNAME_PASSWORD_PAIRS = {
    USER_APP: PASSWORD_APP
}
app = Dash(__name__, suppress_callback_exceptions=True)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)