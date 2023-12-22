import dash
from dash import html
import dash_bootstrap_components as dbc
from views import home


def render() -> html.Div:
    return html.Div(children=[home.make_header(),
                              home.make_signal_view()],
                    style={'display': 'flex',
                           'flexDirection': 'column'}
                    )


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = render()

if __name__ == '__main__':
    app.run(host="0.0.0.0",
            port=8050,
            debug=True)
