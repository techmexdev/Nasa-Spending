import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

def plot_data():
    df = pd.read_csv('/home/yelsek/Documents/python/'
                     'nasa_spending/nasa_spending_1958_present.csv')
    print(df)

if __name__ == '__main__':
    plot_data()
