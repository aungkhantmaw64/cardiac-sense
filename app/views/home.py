import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback
from plotly import express

from models import database


database_explorer = database.Explorer()

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
        {"time_s":[],
         "voltage_mV":[]},
        x="time_s",
        y="voltage_mV")

    available_datasets = database_explorer.get_available_datasets()
    available_records = database_explorer.get_available_records(
        available_datasets[0])


    signal_input = dbc.Card(
        [html.Label("Database"),
         dcc.Dropdown(available_datasets,
                      available_datasets[0],
                      id="database-dropdown"),
         html.Br(),
         html.Label("Record Name"),
         dcc.Dropdown(available_records,
                      available_records[0],
                      id="record-name-dropdown")],
        outline=True,
        style={"padding": 10,
               "flex": 1,
               "border-style":"solid",
               "border-color":"#B80000"
               },
    )
    signal_output = dbc.Card(
        [dcc.Graph(figure=signal_figure,
                   id="signal-figure")],
        outline=True,
        style={"padding": 10,
               "flex": 4,
               "border-style":"solid",
               "border-color":"#B80000"
               },
    )

    return dbc.Card([
        dbc.CardHeader("Single Record Analysis",
                       style={"background-color":"white"}),
        dbc.CardBody([
            signal_input,
            signal_output],
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
    Output("signal-figure","figure"),
    Input("database-dropdown", "value"),
    Input("record-name-dropdown", "value")
)
def update_record_signal(database_name, record_name):
    record_signal = database.PhysionetRecord(
        database_explorer.get_record_path(database_name, record_name)
    ) 
    fig = express.line(
        record_signal.translate(),
        x="time_s",
        y="voltage_mV",
        title=f"Record: {record_name} Database: {database_name}")

    return fig