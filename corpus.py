import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Corpus:
    # crunch down data until it comprises a refreshed database or database-like schema
    def __init__(self):
        self.set_abscombe_quartet()
        self.gapminder: pd.DataFrame = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


    def set_abscombe_quartet(self) -> None:
        # load Anscombe's Quartet, as illustrated by matplotlib
        x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
        y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
        y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
        y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
        x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
        y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

        self.abscombe_quartet = {
            'I': (x, y1),
            'II': (x, y2),
            'III': (x, y3),
            'IV': (x, y4)
        }
