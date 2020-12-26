import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import Panel, Tabs
output_file('bit.html')
data = pd.read_csv('data/BitcoinHeistData.csv')

data = data.sort_values(by=['year', 'day'])
data['date'] = pd.to_datetime(data.year*1000+data.day, format='%Y%j')
data2 = data['day'].groupby(data['year']).count()

data2.index = data2.index.astype(str)
p = figure(x_range=data2.index.to_numpy(), plot_height=300, title="Number of days transactions per year", x_axis_label="years", y_axis_label="days transactions")
p.left[0].formatter.use_scientific = False
p.vbar(x=data2.index, top=data2, width=0.8)
tab = Panel(child=p, title='year')
show(Tabs(tabs=[tab]))
