import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
data = Data([
    Pie(
        domain=dict(
            x=[0, 1],
            y=[0, 1]
        ),
        labels=['Assamese (Asamiya)', 'Bengali', 'Bodo', 'Dogri', 'Gujarati', 'Hindi', 'Kannada', 'Kashmiri', 'Konkani', 'Maithili', 'Malayalam', 'Manipuri(includes Meitei)', 'Marathi', 'Nepali', 'Odia', 'Punjabi', 'Sanskrit', 'Santali', 'Sindhi', 'Tamil', 'Telugu', 'Urdu'],
        name='Col2',
        uid='84247a',
        values=[13, 83, 1.4, 2.3, 46, '340', 55, 5.5, 2.5, 12.2, 33, 1.5, 72, 2.9, 32, 29, 0.001, 6.5, 2.5, 61, 74, 52]
    )
])
layout = Layout(
    autosize=True,
    height=726,
    title='Languages Spoken By Percentage In India',
    width=1044
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
