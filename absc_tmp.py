import plotly.graph_objects as go
from plotly.subplots import make_subplots

from data.corpus import Corpus


corpus = Corpus()
aq1_to_4 = corpus.anscombe_quartet

fig = make_subplots(rows=2, cols=2, start_cell="bottom-left", subplot_titles=("III", "IV","I", "II"))

fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="I"].x, y=aq1_to_4[aq1_to_4.roman_cat=="III"].y3, mode="markers"), row=1, col=1)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="IV"].x4, y=aq1_to_4[aq1_to_4.roman_cat=="IV"].y4, mode="markers"), row=1, col=2)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="III"].x, y=aq1_to_4[aq1_to_4.roman_cat=="I"].y1, mode="markers"), row=2, col=1)
fig.add_trace(go.Scatter(x=aq1_to_4[aq1_to_4.roman_cat=="II"].x, y=aq1_to_4[aq1_to_4.roman_cat=="II"].y2, mode="markers"), row=2, col=2)

fig.update_layout(height=600, width=600, title_text="Anscombe's quartet")

fig.show()


# need a table that shows: mean (7.5), standard deviation (1.94), correlation or maybe slope (0.82),