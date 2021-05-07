import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral3
output_file('bitcoin_timeseries.html')
import datetime
import sys

df = pd.read_csv('bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv')

# convert Epoch time to datetime format
df['Timestamp'] = pd.to_datetime(df['Timestamp'],unit='s')
df['volume_btc'] = df['Volume_(BTC)']
print(df.head())
print(df.dtypes)

source = ColumnDataSource(df)
p = figure(x_axis_type='datetime', title = "Bitcoin Prices")
p.line(x='Timestamp', y='Weighted_Price', line_width=2, source=source, legend_label='Weighted_Price')
p.yaxis.axis_label = 'Bitcoin Price'

p.add_tools(HoverTool(
    tooltips=[
        ('Timestamp', '@Timestamp{%Y-%m-%d %H:%M:%S}'),
        ('Open', '@Open{0.00}'),
        ('High', '@High{0.00}'),
        ('Low', '@Low{0.00}'),
        ('Close', '@Close{0.00}'),
        ('volume_btc', '@volume_btc{0.00}'),
        ('Weighted_Price', '@Weighted_Price{0.00}'),
    ],

    formatters={
        '@Timestamp': 'datetime'
    },

    # display a tooltip whenever the cursor is vertically in line with a glyph
    mode='vline'
))

show(p)