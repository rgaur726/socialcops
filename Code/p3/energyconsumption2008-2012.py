import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Bar(
    x=['Coal', 'Natural Gas', 'Petroleum', 'Renewable Electricity'],
    y=['10.612', '1.576', '6.03', '1.295'],
    name='2008',
    uid='058d66'
)
trace2 = Bar(
    x=['Coal', 'Natural Gas', 'Petroleum', 'Renewable Electricity'],
    y=['11.894', '1.958', '6.231', '1.287'],
    name='2009',
    uid='fc85f5'
)
trace3 = Bar(
    x=['Coal', 'Natural Gas', 'Petroleum', 'Renewable Electricity'],
    y=['12.109', '2.369', '6.698', '1.404'],
    name='2010',
    uid='c5fbcd'
)
trace4 = Bar(
    x=['Coal', 'Natural Gas', 'Petroleum', 'Renewable Electricity'],
    y=['12.46', '2.357', '7.003', '1.681'],
    name='2011',
    uid='9342ab'
)
trace5 = Bar(
    x=['Coal', 'Natural Gas', 'Petroleum', 'Renewable Electricity'],
    y=['12.891', '2.205', '7.328', '1.522'],
    name='2012',
    uid='79fe7b'
)
data = Data([trace1, trace2, trace3, trace4, trace5])
layout = Layout(
    autosize=True,
    height=505,
    title='India Energy Consumption from 2008-2012',
    width=1121,
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 3.5],
        title='Types of Energy',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 13.569473684210527],
        title='Energy Consumption in Quadrillion Btu',
        type='linear'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
