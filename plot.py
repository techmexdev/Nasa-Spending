import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import Scatter, Figure, Layout

import numpy as np
import pandas as pd

def test_plot():
    filename = '/home/yelsek/Documents/python/nasa_spending/'\
        'nasa_spending_inflation_adjusted_without_presidents.csv' 

    df = pd.read_csv(filename)
    data_dict = df.to_dict()

    amt_spend_on_nasa = [value for value in
        data_dict['amt_spend_nasa_millions'].values()]
    years = [year for year in 
        data_dict['Year'].values()]
    total_fed_spending = [amt for amt in 
        data_dict['total_fed_spend_millions'].values()]
    percent_nasa = [percent for percent in 
        data_dict['%_spend_nasa'].values()]

    nasa_spending_graph = Scatter(x=years,
        y=amt_spend_on_nasa)
    total_fed_spending_graph = Scatter( 
        x=years, y=total_fed_spending)
    percent_nasa_spending_graph = Scatter(
        x=years, y=percent_nasa)
    federal_spending_vs_nasa = Scatter( 
        x=total_fed_spending, y=amt_spend_on_nasa)

    which = raw_input('Choose graph: nasa_spending, fed_spending, percent_nasa,'
                  'fed_vs_nasa:\n')
    if which == 'nasa_spending':
        plot([nasa_spending_graph])
    elif which == 'fed_spending':
        plot([total_fed_spending_graph])
    elif which == 'percent_nasa':
        plot([percent_nasa_spending_graph])
    else:
        plot([federal_spending_vs_nasa])


if __name__ == '__main__':
    with_pres = '/home/yelsek/Documents/python/nasa_spending/'\
        'nasa_spending_inflation_adjusted'
    without_pres = '/home/yelsek/Documents/python/nasa_spending/'\
        'nasa_spending_inflation_adjusted_without_presidents.csv' 
    
    test_plot()

