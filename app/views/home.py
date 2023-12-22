import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from plotly import express

from models import database


def make_header() -> dbc.NavbarSimple:
    return dbc.NavbarSimple(
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



def make_signal_view() -> html.Div:
    signal_figure = express.line(
        {"x": [1, 2, 3],
         "y": [4, 4, 4]},
        x="x",
        y="y")

    database_explorer = database.Explorer()
    available_datasets = database_explorer.get_available_datasets()
    available_records = database_explorer.get_available_records(
        available_datasets[0])


    signal_input = dbc.Card(
        [html.Label("Database"),
         dcc.Dropdown(available_datasets,
                      available_datasets[0]),
         html.Br(),
         html.Label("Record Name"),
         dcc.Dropdown(available_records,
                      available_records[0])],
        outline=True,
        color="primary",
        style={"padding": 10,
               "flex": 1}
    )
    signal_output = dbc.Card(
        [dcc.Graph(figure=signal_figure)],
        outline=True,
        color="primary",
        style={"padding": 10,
               "flex": 4}
    )

    return dbc.Card([
        dbc.CardHeader("Single Record Analysis"),
        dbc.CardBody([
            signal_input,
            signal_output],
            style={"display": "flex",
                   "flexDirection": "row"})])
