import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Scatter(
    x=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'A&NIslands', 'Chandigarh', 'Dadra & Nagar   Haveli', 'Daman & Diu', 'Lakshadweep', 'Puducherry'],
    y=['275069', '83743', '78438', '94163', '135191', '1483', '3702', '196022', '44212', '55673', '222236', '79714', '191791', '38863', '308245', '307713', '22327', '22429', '21081', '16579', '155707', '50362', '342239', '7096', '130058', '10486', '240928', '53483', '88752', '8249', '114', '491', '112', '32', '480'],
    error_x=ErrorX(
        copy_ystyle=True
    ),
    error_y=ErrorY(
        color='rgb(0, 67, 88)',
        thickness=1,
        width=1
    ),
    fill='none',
    fillcolor='rgba(0, 67, 88, 0.5)',
    line=Line(
        color='rgb(19, 27, 88)',
        dash='solid',
        width=6
    ),
    marker=Marker(
        color='rgb(19, 27, 88)',
        line=Line(
            color='white',
            width=6
        ),
        size=6,
        symbol='dot'
    ),
    mode='lines',
    name='Geographical Area in sq. Km',
    uid='29fba8'
)
trace2 = Scatter(
    x=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Orissa', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'A&NIslands', 'Chandigarh', 'Dadra & Nagar   Haveli', 'Daman & Diu', 'Lakshadweep', 'Puducherry'],
    y=['46389', '67410', '27673', '6845', '55674', '176', '2219', '14619', '1608', '14679', '22539', '22977', '36194', '17300', '77700', '50646', '17090', '17275', '19117', '13318', '48903', '1764', '16087', '3359', '23625', '7977', '14338', '24496', '12995', '6724', '17', '211', '6', '27', '50'],
    error_x=ErrorX(
        copy_ystyle=True
    ),
    error_y=ErrorY(
        color='rgb(31, 138, 112)',
        thickness=1,
        width=1
    ),
    fill='none',
    line=Line(
        color='rgb(0, 167, 141)',
        dash='solid',
        width=6
    ),
    marker=Marker(
        color='rgb(0, 167, 141)',
        line=Line(
            color='white',
            width=6
        ),
        size=6,
        symbol='dot'
    ),
    mode='lines',
    name='Forest Cover in sq. Km',
    uid='4dc767'
)
data = Data([trace1, trace2])
layout = Layout(
    autosize=True,
    dragmode='zoom',
    font=Font(
        family='"Droid Sans", sans-serif'
    ),
    height=486,
    legend=Legend(
        x=0.7380729653882133,
        y=1.084967320261438
    ),
    paper_bgcolor='rgb(213, 226, 233)',
    plot_bgcolor='rgb(213, 226, 233)',
    showlegend=True,
    title='State Wise Forest Cover in India in 2011',
    width=1229,
    xaxis=XAxis(
        autorange=False,
        gridcolor='white',
        gridwidth=1,
        range=[-0.5966150305284508, 38.252833188020624],
        showgrid=False,
        tickfont=dict(
            color='black',
            family='"Verdana", monospace',
            size=10
        ),
        title='State/UT',
        titlefont=dict(
            color='black',
            family='"Verdana", monospace',
            size=12
        ),
        type='category',
        zeroline=False
    ),
    yaxis=YAxis(
        autorange=False,
        gridcolor='white',
        gridwidth=1,
        range=[-61234.086747389054, 373261.44306237216],
        showgrid=True,
        tickfont=dict(
            color='black',
            family='"Verdana", monospace',
            size=10
        ),
        ticks='',
        title='Geographical Area in Sq. Km',
        titlefont=dict(
            color='black',
            family='"Verdana", monospace',
            size=12
        ),
        type='linear',
        zeroline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
