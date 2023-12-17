import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from plotly import express

header = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Analysis",
                                     href="#"),
                dbc.DropdownMenuItem("Deep Learning",
                                     href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="View",
        ),
        dbc.NavItem(dbc.NavLink("About", href="#")),

    ],
    brand="CardiacSense",
    brand_href="#",
    color="#B80000",
    dark=True,
)

signal_figure = express.line(
    {"x": [1, 2, 3],
     "y": [4, 4, 4]},
    x="x",
    y="y")

signal_input = html.Div(
    [html.Label("Database"),
     dcc.Dropdown(["MIT-BIH", "Other"], "MIT-BIH"),
     html.Br(),
     html.Label("Record Name"),
     dcc.Dropdown(["100", "101", "200"], "100")],
    style={"padding": 10,
           "flex": 1}
)
signal_output = html.Div(
    [dcc.Graph(figure=signal_figure)],
    style={"padding": 10,
           "flex": 4}
)

signal_view = html.Div([
    html.H3("Single Record Analysis",
            style={"textAlign":"center",
                   "padding":2}),
    html.Div([
    signal_input,
    signal_output],
    style={"display": "flex",
           "flexDirection": "row"})
])
