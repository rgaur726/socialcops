import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Bar(
    x=['Facebook Messenger', 'Hike', 'BBM', 'Viber', 'WeChat', 'Line', 'WhatsApp'],
    y=[0.826499, 0.928816, 0.664119, 1.292612, 0.891354, 1.584107, 6.39724],
    marker=Marker(
        color='#ECECEC'
    ),
    name='Avg WiFi Data Used'
)
trace2 = Bar(
    x=['Facebook Messenger', 'Hike', 'BBM', 'Viber', 'WeChat', 'Line', 'WhatsApp'],
    y=[0.738456, 0.72017, 0.42394, 0.526172, 0.305926, 0.485156, 1.751087],
    marker=Marker(
        color='#C9442A'
    ),
    name='Avg Cellular Data Used'
)
data = Data([trace1, trace2])
layout = Layout(
    barmode='stack',
    title='Avg. Data Used on Popular Messenger Apps in India',
    xaxis=XAxis(
        linecolor='#eee',
        zeroline=False
    ),
    yaxis=YAxis(
        linecolor='#fff',
        title='Avg. Data Used (MB)',
        zeroline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
