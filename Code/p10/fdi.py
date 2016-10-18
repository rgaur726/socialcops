import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
data = Data([
    Scatter(
        x=['2011-2012', '2012-2013', '2013-2014', '2014-2015'],
        y=['11,097', '7,134', '9,199', '1,799'],
        error_x=ErrorX(
            color='black',
            copy_ystyle=True,
            thickness='1',
            width='2'
        ),
        error_y=ErrorY(
            color='rgb(0, 67, 88)',
            thickness=1,
            visible=False,
            width=1
        ),
        fill='none',
        line=Line(
            color='rgb(4, 158, 215)',
            dash='solid',
            shape='linear',
            width=3
        ),
        marker=Marker(
            color='rgb(4, 158, 215)',
            line=Line(
                color='white',
                width=0
            ),
            maxdisplayed=0,
            opacity=1,
            size=6,
            symbol='dot'
        ),
        name='US$ million',
        opacity=1,
        uid='0c7863'
    )
])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1.9981920449979909,
            y=9644.481294236602,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='#444',
                family='"Open Sans", verdana, arial, sans-serif',
                size=12
            ),
            opacity=1,
            showarrow=False,
            text='9,199',
            textangle=0,
            xref='x',
            yref='y'
        ),
        Annotation(
            x=2.998593812776215,
            y=2342.7152005392645,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='#444',
                family='"Open Sans", verdana, arial, sans-serif',
                size=12
            ),
            opacity=1,
            showarrow=False,
            text='1,799',
            textangle=0
        ),
        Annotation(
            x=0.9977902772197668,
            y=7764.198179979778,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='#444',
                family='"Open Sans", verdana, arial, sans-serif',
                size=12
            ),
            opacity=1,
            showarrow=False,
            text='7,134',
            textangle=0
        ),
        Annotation(
            x=0.005423865006026318,
            y=11524.764408493429,
            bgcolor='rgba(0, 0, 0, 0)',
            bordercolor='rgba(0, 0, 0, 0)',
            borderpad=1,
            borderwidth=1,
            font=Font(
                color='#444',
                family='"Open Sans", verdana, arial, sans-serif',
                size=12
            ),
            opacity=1,
            showarrow=False,
            text='11,097',
            textangle=0
        ),
        Annotation(
            x=2.7213740458015265,
            y=13607.60753014234,
            ax=-10,
            ay=-30,
            font=Font(
                color='rgb(102, 102, 102)'
            ),
            showarrow=False,
            text='Resource: Reserve Bank in India '
        )
    ]),
    autosize=True,
    bargap=0.2,
    dragmode='zoom',
    font=Font(
        color='#444',
        family='"Droid Sans", sans-serif',
        size=12
    ),
    height=600,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.02,
        y=1,
        bgcolor='white',
        bordercolor='black',
        borderwidth=0,
        font=Font(
            color='rgb(105, 100, 124)'
        )
    ),
    paper_bgcolor='rgb(213, 226, 233)',
    plot_bgcolor='rgb(213, 226, 233)',
    separators='.,',
    showlegend=False,
    title='Foreign Direct Investment (FDI) in India',
    titlefont=dict(
        color='#444',
        family='"Open Sans", verdana, arial, sans-serif',
        size=17
    ),
    width=1044,
    xaxis=XAxis(
        autorange=True,
        gridcolor='white',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        range=[-0.1825275980205558, 3.1825275980205556],
        rangemode='tozero',
        showgrid=False,
        showline=False,
        showticklabels=True,
        tickangle='auto',
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='black',
            family='"Verdana", monospace',
            size=10
        ),
        ticklen=6,
        tickmode='auto',
        ticks='',
        title='Year',
        titlefont=dict(
            color='black',
            family='"Verdana", monospace',
            size=12
        ),
        type='category',
        zeroline=False,
        zerolinecolor='#444',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        autorange=True,
        exponentformat='B',
        gridcolor='white',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        range=[0, 13905.584337371734],
        rangemode='tozero',
        showexponent='all',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickangle='auto',
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='black',
            family='"Verdana", monospace',
            size=10
        ),
        ticklen=6,
        tickmode='auto',
        ticks='',
        title='US$ million',
        titlefont=dict(
            color='black',
            family='"Verdana", monospace',
            size=12
        ),
        zeroline=False,
        zerolinecolor='#444',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
