import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

# df = pd.read_csv(infile, parse_dates={'datetime': ['date', 'time']}, date_parser=dateparse)
df = pd.read_csv('result.csv', parse_dates=['dateTime'], index_col='dateTime') 
df = df.sort_index()
print(df.head())

traces_line = []

for col in df.columns:
	traces_line.append(go.Scatter(
		x = df.index,
		y = df[col],
		name = col,
		connectgaps = True
	))

layout_line = go.Layout(
    title='Twitter Users Happiness Line Chart',
    yaxis=dict(title='Happiness Index'),
    xaxis=dict(title='Date Time')
)

fig_line = go.Figure(data=traces_line, layout=layout_line)

py.plot(fig_line, filename='line_chart.html')

traces_heat = [
	go.Heatmap(
		z = df.T.values.tolist(),
		x = df.index,
		y = df.columns,
		# colorscale = 'Viridis'
		colorscale=[[0.0, 'rgb(146,168,209)'], [0.1111111111111111, 'rgb(168,185,218)'], [0.2222222222222222, 'rgb(190,203,227)'], [0.3333333333333333, 'rgb(211,220,237)'], [0.4444444444444444, 'rgb(233,238,246)'], [0.5555555555555556, 'rgb(253,244,244)'], [0.6666666666666666, 'rgb(252,234,233)'], [0.7777777777777778, 'rgb(250,223,223)'], [0.8888888888888888, 'rgb(249,213,212)'], [1.0, 'rgb(247,202,201)']]
	)
]

layout_heat = go.Layout(
    title='Twitter Users Happiness Heatmap',
    xaxis = dict(title='Date Time', nticks=6),
    yaxis = dict(title='Users', ticks='')
)

fig_heat = go.Figure(data=traces_heat, layout=layout_heat)

py.plot(fig_heat, filename='heatmap.html')