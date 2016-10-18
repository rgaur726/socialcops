import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Bar(
    x=['Andaman and Nicobar Islands', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Jharkhand', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Mizoram', 'Nagaland', 'Odisha', 'Rajasthan', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[30.3, 18.53, 13.49, 9.41, 23.48, 21.82, 12.93, 47.18, 15.23, 13.16, 27.91, 12.57, 31.14, 10.52, 15.8, 8.5, 18.93, 12.02, 24.61],
    marker=Marker(
        color='rgb(213,62,79)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='1951',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace2 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Delhi', 'Goa', 'Gujarat', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Rajasthan', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[40.07, 21.19, 7.13, 32.95, 21.95, 18.14, 61.95, 35.41, 31.47, 12.95, 21.14, 29.8, 55.08, 27.15, 21.41, 35.08, 36.04, 26.92, 44.01, 21.95, 21.66, 43.65, 18.12, 36.39, 20.24, 18.05, 20.87, 34.46],
    marker=Marker(
        color='rgb(252,141,89)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='1961',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace3 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[51.15, 24.57, 11.29, 33.94, 23.17, 70.43, 24.08, 18.13, 65.08, 51.96, 36.95, 25.71, 21.71, 23.87, 36.83, 69.75, 51.76, 27.27, 45.77, 38.47, 29.49, 53.8, 33.78, 26.18, 53.38, 34.12, 22.57, 17.74, 45.4, 30.98, 33.26, 23.99, 38.86],
    marker=Marker(
        color='rgb(254,224,139)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='1971',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace4 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[63.19, 35.66, 25.55, 32.32, 74.8, 32.63, 32.9, 71.94, 65.71, 44.92, 37.13, 30.64, 35.03, 46.21, 78.85, 68.42, 38.63, 57.24, 49.66, 42.05, 59.88, 50.28, 33.62, 65.14, 43.37, 30.11, 34.05, 54.39, 50.1, 46.06, 32.65, 48.65],
    marker=Marker(
        color='rgb(255,255,191)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='1981',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace5 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[73.02, 44.08, 41.59, 52.89, 37.49, 77.81, 42.91, 40.71, 71.2, 75.29, 75.51, 61.29, 55.85, 63.86, 41.39, 56.04, 89.81, 81.78, 44.67, 64.87, 59.89, 49.1, 82.26, 61.65, 49.09, 74.74, 58.51, 38.55, 56.94, 62.66, 60.44, 57.75, 40.71, 57.7],
    marker=Marker(
        color='rgb(230,245,152)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='1991',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace6 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[81.3, 60.47, 54.34, 63.25, 47, 81.94, 64.66, 57.63, 78.18, 81.67, 82.01, 69.14, 67.91, 76.48, 55.52, 53.56, 66.64, 90.86, 86.66, 63.74, 76.88, 70.53, 62.56, 88.8, 66.59, 63.08, 81.24, 69.65, 60.41, 68.81, 73.45, 73.19, 71.62, 56.27, 68.64],
    marker=Marker(
        color='rgb(153,213,148)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='2001',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
trace7 = Bar(
    x=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal'],
    y=[86.6, 67, 65.4, 72.2, 61.8, 86, 70.3, 76.2, 87.1, 86.2, 88.7, 78, 75.6, 82.8, 67.2, 66.4, 75.4, 94, 91.8, 69.3, 82.3, 76.9, 74.4, 91.3, 79.6, 72.9, 85.8, 75.8, 66.1, 81.4, 80.1, 87.2, 78.8, 67.7, 76.3],
    marker=Marker(
        color='rgb(50,136,189)',
        line=Line(
            color='rgb(0,0,0)',
            width=1
        )
    ),
    name='2011',
    opacity=0.4,
    showlegend=True,
    xaxis='x1',
    yaxis='y1'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=1.05,
            y=0.52,
            showarrow=False,
            text='<b>Year</b>',
            textangle=0,
            xanchor='center',
            xref='paper',
            yref='paper'
        )
    ]),
    barmode='stack',
    legend=Legend(
        x=1.05,
        y=0.5,
        bgcolor='rgb(255,255,255)',
        bordercolor='transparent',
        font=Font(
            family=''
        ),
        xanchor='center',
        yanchor='top'
    ),
    margin=Margin(
        r=10
    ),
    paper_bgcolor='rgb(255,255,255)',
    plot_bgcolor='rgb(229,229,229)',
    showlegend=[True, True],
    title='All India Literacy Rate (State-wise)',
    titlefont=dict(
        family=''
    ),
    xaxis=XAxis(
        gridcolor='rgb(255,255,255)',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickangle=-70,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        title=' ',
        type='category',
        zeroline=False
    ),
    yaxis=YAxis(
        gridcolor='rgb(255,255,255)',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        title='Literacy Rate',
        type='linear',
        zeroline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
