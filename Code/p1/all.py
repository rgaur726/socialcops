import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = Bar(
    x=[0, 0.43473009999999995, 0, 0, 0.6812533000000001, 1.5007393999999998, 0, 2.0179866, 0.3189589, 3.4046329, 2.8996216, 0, 1.9542028, 0, 7.2598557999999995, 4.0867444, 8.1269728],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#1f77b4',
        line=Line(
            color='#444'
        )
    ),
    name='Cardiovascular diseases',
    opacity=0.6,
    orientation='h',
    uid='c8ee5c'
)
trace2 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0.7732088, 0, 0, 0, 0.4142435, 0, 0, 0, 0, 2.0308509, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#ff7f0e',
        line=Line(
            color='#444'
        )
    ),
    name='Chronic respiratory diseases',
    opacity=0.6,
    orientation='h',
    uid='83230e'
)
trace3 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0.8965818999999999, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#2ca02c',
        line=Line(
            color='#444'
        )
    ),
    name='Cirrhosis',
    opacity=0.6,
    orientation='h',
    uid='be928c'
)
trace4 = Bar(
    x=[0, 0.0174578, 0, 0, 1.0840026, 0.24771939999999998, 0, 0.7987339, 0.0366026, 0, 0.11076630000000001, 0, 2.2836446, 0, 0.5321062, 0, 0.6779011999999999],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#d62728',
        line=Line(
            color='#444'
        )
    ),
    name='Diabetes, urogenital, blood, and endocrine diseases',
    opacity=0.6,
    orientation='h',
    uid='816227'
)
trace5 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0.0596893, 0, 0.339994, 4.8885508, 0, 3.9603960000000002, 0, 1.503528, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#9467bd',
        line=Line(
            color='#444'
        )
    ),
    name='Diarrhea, lower respiratory, and other common infectious diseases',
    opacity=0.6,
    orientation='h',
    uid='5bd5d1'
)
trace6 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0.058659199999999995, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#8c564b',
        line=Line(
            color='#444'
        )
    ),
    name='Digestive diseases',
    opacity=0.6,
    orientation='h',
    uid='d86396'
)
trace7 = Bar(
    x=[0, 0, 0.0345998, 0.6037208000000001, 0, 0, 0, 0, 0.5063779, 0, 0.3307987, 0, 0.9443794, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#e377c2',
        line=Line(
            color='#444'
        )
    ),
    name='HIV/AIDS and tuberculosis',
    opacity=0.6,
    orientation='h',
    uid='fb19e2'
)
trace8 = Bar(
    x=[0, 0, 0.00646727, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0511126, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#7f7f7f',
        line=Line(
            color='#444'
        )
    ),
    name='Maternal disorders',
    opacity=0.6,
    orientation='h',
    uid='7cd8bb'
)
trace9 = Bar(
    x=[0, 0.014648600000000001, 0.49790900000000005, 0, 0, 0, 0, 0, 0.6257585999999999, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#bcbd22',
        line=Line(
            color='#444'
        )
    ),
    name='Mental and substance use disorders',
    opacity=0.6,
    orientation='h',
    uid='58db25'
)
trace10 = Bar(
    x=[0, 0, 0, 0, 9.53e-05, 0, 0.6317066, 0.11850129999999999, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#17becf',
        line=Line(
            color='#444'
        )
    ),
    name='Musculoskeletal disorders',
    opacity=0.6,
    orientation='h',
    uid='10137d'
)
trace11 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#1f77b4',
        line=Line(
            color='#444'
        )
    ),
    name='Neglected tropical diseases and malaria',
    opacity=0.6,
    orientation='h',
    uid='011338'
)
trace12 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#ff7f0e',
        line=Line(
            color='#444'
        )
    ),
    name='Neonatal disorders',
    opacity=0.6,
    orientation='h',
    uid='b64dff'
)
trace13 = Bar(
    x=[0, 0.029274200000000004, 0, 0.2454346, 0, 0.0474087, 0.037603199999999996, 0.0965382, 0.249054, 0, 0.10845629999999999, 0, 0, 0, 0, 0.15909420000000002, 0.4895170999999999],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#2ca02c',
        line=Line(
            color='#444'
        )
    ),
    name='Neoplasms',
    opacity=0.6,
    orientation='h',
    uid='37584f'
)
trace14 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0.0381318, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#d62728',
        line=Line(
            color='#444'
        )
    ),
    name='Neurological disorders',
    opacity=0.6,
    orientation='h',
    uid='d5c5bf'
)
trace15 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2.8206317999999997, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#9467bd',
        line=Line(
            color='#444'
        )
    ),
    name='Nutritional deficiencies',
    opacity=0.6,
    orientation='h',
    uid='bc9576'
)
trace16 = Bar(
    x=[0, 0, 0, 0.4894294, 0, 0, 0, 0, 0.000540419, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#8c564b',
        line=Line(
            color='#444'
        )
    ),
    name='Other communicable, maternal, neonatal, and nutritional diseases',
    opacity=0.6,
    orientation='h',
    uid='2eb432'
)
trace17 = Bar(
    x=[0, 0, 0, 0, 0, 0, 0.3022069, 0, 0, 0, 0, 0, 0, 0, 0, 0.0535179, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#e377c2',
        line=Line(
            color='#444'
        )
    ),
    name='Other non-communicable diseases',
    opacity=0.6,
    orientation='h',
    uid='d42b61'
)
trace18 = Bar(
    x=[0.29211940000000003, 0, 0, 0, 0, 0, 0.19951979999999997, 0, 0.31272609999999995, 0, 0, 0, 0, 0, 0, 0, 0],
    y=['Low bone mineral density', 'Other environmental risks', 'Sexual abuse and violence', 'Unsafe sex', 'Low glomerular filtration rate', 'Low physical activity', 'Occupational risks', 'High body-mass index', 'Alcohol and drug use', 'High total cholesterol', 'Tobacco smoke', 'Unsafe water, sanitation, and handwashing', 'High fasting plasma glucose', 'Child and maternal malnutrition', 'High systolic blood pressure', 'Air pollution', 'Dietary risks'],
    marker=Marker(
        color='#7f7f7f',
        line=Line(
            color='#444'
        )
    ),
    name='Unintentional injuries',
    opacity=0.6,
    orientation='h',
    uid='ea646d'
)
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18])
layout = Layout(
    autosize=True,
    bargap=0.2,
    bargroupgap=0,
    barmode='stack',
    dragmode='zoom',
    font=Font(
        color='#444',
        family='"Open sans", verdana, arial, sans-serif',
        size=16
    ),
    height=822,
    hidesources=False,
    hovermode='y',
    margin=Margin(
        l=350
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=False,
    title='India, All ages (2013)',
    titlefont=dict(
        color='#444',
        family='"Open sans", verdana, arial, sans-serif',
        size=22
    ),
    width=1620,
    xaxis=XAxis(
        autorange=True,
        exponentformat='B',
        nticks=0,
        range=[0, 9.783569578947368],
        showexponent='all',
        showgrid=False,
        showline=True,
        showticklabels=True,
        tickangle='auto',
        tickfont=dict(
            color='#444',
            family='"Open sans", verdana, arial, sans-serif',
            size=16
        ),
        tickmode='auto',
        ticks='',
        ticksuffix='%',
        title='Percent of total DALYs',
        titlefont=dict(
            color='#444',
            family='"Open sans", verdana, arial, sans-serif',
            size=19
        ),
        type='linear',
        zeroline=False,
        zerolinecolor='#444',
        zerolinewidth=1
    ),
    yaxis=YAxis(
        autorange=True,
        nticks=0,
        range=[-0.5, 16.5],
        rangemode='normal',
        showgrid=False,
        showline=False,
        showticklabels=True,
        tickangle='auto',
        tickfont=dict(
            color='#444',
            family='"Open sans", verdana, arial, sans-serif',
            size=16
        ),
        tickmode='auto',
        ticks='',
        titlefont=dict(
            color='#444',
            family='"Open sans", verdana, arial, sans-serif',
            size=19
        ),
        type='category',
        zeroline=True,
        zerolinecolor='#444',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
