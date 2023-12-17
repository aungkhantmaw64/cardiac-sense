import dash
from dash import html
import dash_bootstrap_components as dbc
from plotly import express

from views import home

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    children=[home.header,
              home.signal_view],
    style={'display': 'flex',
           'flexDirection': 'column'}
)

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=8050,
            debug=True)
