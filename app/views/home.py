import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
from plotly import express

from models import database


database_explorer = database.Explorer()


def render_header() -> dbc.NavbarSimple:
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


def render_signal_view() -> html.Div:
    DEFAULT_DATASET = 0
    DEFAULT_RECORD = 0

    figure = express.line(
        {"time_s": [],
         "voltage_mV": []},
        x="time_s",
        y="voltage_mV")

    available_datasets = database_explorer.get_available_datasets()
    available_records = database_explorer.get_available_records(
        available_datasets[DEFAULT_DATASET])

    inputs = dbc.Card(
        [html.Label("Database"),
         dcc.Dropdown(available_datasets,
                      available_datasets[DEFAULT_DATASET],
                      id="database-dropdown"),
         html.Br(),
         html.Label("Record Name"),
         dcc.Dropdown(available_records,
                      available_records[DEFAULT_RECORD],
                      id="record-name-dropdown")],
        outline=True,
        style={"padding": 10,
               "flex": 1,
               "border-style": "solid",
               "border-color": "#B80000"
               },
    )
    outputs = dbc.Card(
        [dcc.Graph(figure=figure,
                   id="signal-figure")],
        outline=True,
        style={"padding": 10,
               "flex": 4,
               "border-style": "solid",
               "border-color": "#B80000"
               },
    )

    return dbc.Card([
        dbc.CardHeader("Single Record Analysis",
                       style={"background-color": "white"}),
        dbc.CardBody([
            inputs,
            outputs],
            style={"display": "flex",
                   "flexDirection": "row"
                   })]
    )


@callback(
    Output("record-name-dropdown", "options"),
    Output("record-name-dropdown", "value"),
    Input("database-dropdown", "value")
)
def update_record_name_dropdown(database_name):
    return (database_explorer.get_available_records(database_name),
            database_explorer.get_available_records(database_name)[0])


@callback(
    Output("signal-figure", "figure"),
    Input("database-dropdown", "value"),
    Input("record-name-dropdown", "value")
)
def update_signal_view(database_name, record_name):
    MAX_SAMPLE_POINTS = 3000
    ecg_record = database.PhysionetRecord.from_path(
        database_explorer.get_record_path(database_name, record_name)
    )
    signal_of_interest = {
        "time_s": ecg_record.to_dict()["time_s"][:MAX_SAMPLE_POINTS],
        "voltage_mV": ecg_record.to_dict()["voltage_mV"][:MAX_SAMPLE_POINTS]
    }
    fig = express.line(
        signal_of_interest,
        x="time_s",
        y="voltage_mV",
        labels={"time_s":"Time (seconds)",
                "voltage_mV":"Voltage (mV)"},
        title=f"Database: {database_name}, Record: {record_name} ")
    return fig
