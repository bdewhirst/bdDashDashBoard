# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

from corpus import Corpus


# Retrieve corpus
corpus = Corpus()
abs_qrt = corpus.abscombe_quartet
demographics = corpus.gapminder
# demographics = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children="My First App with Data, Graph, and Controls"),
    html.Hr(),
    dcc.RadioItems(
        options=["pop", "lifeExp", "gdpPercap"],
        value="lifeExp",
        id="my-final-radio-item-example",
    ),
    dash_table.DataTable(data=demographics.to_dict("records"), page_size=6),
    dcc.Graph(figure={}, id="my-final-graph-example"),
]


# Add controls to build the interaction
@callback(
    Output(component_id="my-final-graph-example", component_property="figure"),
    Input(component_id="my-final-radio-item-example", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(demographics, x="continent", y=col_chosen, histfunc="avg")
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
