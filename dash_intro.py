import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import yfinance as yf 
import plotly.express as px
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

#Get the data
def get_data(ticker):
    df = yf.download(ticker)
    df.reset_index(inplace=True)
    df = df[["Date", "Close"]]
    return df

get_data("AAPL")


#Build a graph
def build_graph(df):
    return px.line(x=df["Date"], y=df["Close"])


#Build dashboard

app = dash.Dash()


app.layout = html.Div([
    dcc.Dropdown(id="dropdown", 
                options=[
                    {"label":"Beyond meat", "value":"BYND"},
                    {"label":"Moderna", "value":"MRNA"},
                    {"label":"Pfizer", "value":"PFE"}
                ]),
    dcc.Graph(id="graph")
])

@app.callback(
    [Output("graph", "figure")],
    [Input("dropdown", "value")]
)

def build_the_dash(v):
    if v == None:
        raise PreventUpdate
    df = get_data(v)
    fig = build_graph(df)
    return [fig]

app.run_server(debug=True)