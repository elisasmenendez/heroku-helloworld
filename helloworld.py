import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px 


app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        'backgroundColor': '#111111',
        'position':'fixed',
        'width':'100%',
        'height':'100%',
        'top':'0px',
        'left':'0px',
        'z-index':'1000'
    }, 
    children=[   
        html.H2(
            "Simples Dash", 
            style={
                'text-align': 'center',
                'color': '#ffffff'
            }),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph(n):
    df = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)