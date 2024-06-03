from data.corpus import Corpus
from plotly.subplots import make_subplots
from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import plotly.express as px

import plotly.graph_objects as go


corpus = Corpus()
aq1_to_4 = corpus.anscombe_quartet

fig = make_subplots(rows=2, cols=2, start_cell="bottom-left", subplot_titles=("III", "IV","I", "II"))
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="I"].x, y=aq1_to_4[aq1_to_4.roman_cat=="III"].y3, mode="markers"), row=1, col=1)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="IV"].x4, y=aq1_to_4[aq1_to_4.roman_cat=="IV"].y4, mode="markers"), row=1, col=2)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="III"].x, y=aq1_to_4[aq1_to_4.roman_cat=="I"].y1, mode="markers"), row=2, col=1)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="II"].x, y=aq1_to_4[aq1_to_4.roman_cat=="II"].y2, mode="markers"), row=2, col=2)
fig.update_layout(height=600, width=600, title_text="Anscombe's quartet")

# fig.show()

image_path = 'assets/sew.png'

app = Dash()

# App layout
app.layout = [
    html.Div(children="My First App with Data, Graph, and Controls"),
    html.Hr(),
    # dcc.RadioItems(
    #     options=["pop", "lifeExp", "gdpPercap"],
    #     value="lifeExp",
    #     id="my-final-radio-item-example",
    # ),
    html.Img(src=image_path),
    # dash_table.DataTable(data=demographics.to_dict("records"), page_size=6),
    dcc.Graph(figure={}, id="my-final-graph-example"),
    dcc.Graph(figure=fig)
]



# # Add controls to build the interaction
# @callback(
#     Output(component_id="my-final-graph-example", component_property="figure"),
#     Input(component_id="my-final-radio-item-example", component_property="value"),
# )
# def update_graph(col_chosen):
#     fig = px.histogram(demographics, x="continent", y=col_chosen, histfunc="avg")
#     return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
