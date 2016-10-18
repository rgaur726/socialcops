import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[15758621, 16409396],
    name='Total number of pregnant women Registered for ANC 2014-15',
    uid='df5bbb'
)
trace2 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[1278311, 1627111],
    name='Number of Home deliveries 2014-15',
    uid='d21954'
)
trace3 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[10614395, 11316541],
    name='Total reported deliveries 2014-15',
    uid='d270d4'
)
trace4 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[10775279, 11663685],
    name='Total Number of reported live births 2014-15',
    uid='a07c9e'
)
trace5 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[11322733, 12128588],
    name='Number of fully immunized children 9-11 months 2014-15',
    uid='a5e729'
)
trace6 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[2283543, 1928984],
    name='Number of Major Operations 2014-15',
    uid='5e6bd2'
)
trace7 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[3930482, 3175949],
    name='Number of Minor Operations 2014-15',
    uid='030ede'
)
trace8 = Bar(
    x=['2014-2015', '2013-2014'],
    y=[93589, 86260],
    name='Total Number of Infant Deaths reported 2014-15',
    uid='ab1c78'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8])
layout = Layout(
    autosize=True,
    height=536,
    title='India Health Parameter',
    width=1121,
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 1.5],
        title='Yearly Data',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        dtick=1000000,
        range=[0, 17273048.42105263],
        tickmode='linear',
        title='Value in Number',
        type='linear'
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
