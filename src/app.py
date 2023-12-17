import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    children = [
       html.H1(children = "CardiacSense",
               style={"textAlign":"center", 
                      "padding":10,"flex":1}),
        html.Div(
           children=[
               html.Label("Database"),
               dcc.Dropdown(['DatabaseA', 'DatabaseB', 'DatabaseC'], 'DatabaseA', id='abc-dropdown'),
               html.Br(),
               html.Label("Record"),
               dcc.Dropdown(['Record001','Record002','Record003'], 'Record001')
           ],
           style={"padding":10,"flex":1}
       ),
       html.Div
       (
           children=[
               dcc.Graph()
           ],
           style={"padding":10,"flex":1}
       )    
    ],
    style = {"display":"flex","flexDirection":"column"}
)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8050, debug=True)