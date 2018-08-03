import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

app = dash.Dash()
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

y_saving = [41.6, 45.1, 43.9, 52.4, 46.7]
y_net_worth = [2890, 115887, 186528, 700838, 1593452]
x_saving = ['Aut. Online', 'Authenticated', 'Completed', 'Started', 'Visits']
x_net_worth = ['Aut. Online', 'Authenticated', 'Completed', 'Started', 'Visits']

trace0 = go.Bar(
    x=y_saving,
    y=x_saving,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Relative Funnel Internet',
    orientation='h',
)

trace1 = go.Scatter(
    x=y_net_worth,
    y=x_net_worth,
    mode='lines+markers',
    line=dict(
        color='rgb(128, 0, 128)'),
    name='Absolute Funnel Internet',
)

data0 = [trace0]
data1 = [trace1]

layout = dict(
    showlegend=True,
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 1],
    ),
    legend=dict(
        x=0.029,
        y=1.038,
        font=dict(
            size=10
        )

    ),
    margin=dict(
        l=85,
        r=10,
        t=70,
        b=70
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)'
)

layout2 = dict(
    showlegend=True,
    yaxis=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='rgba(102, 102, 102, 0.8)',
        linewidth=2,
        domain=[0, 0.85]
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.01, 1],
        side='top',
        dtick=250000
    ),
    legend=dict(
        x=0.029,
        y=1.038,
        font=dict(
            size=10
        )
    ),
    margin=dict(
        l=20,
        r=20,
        t=70,
        b=70
    ),
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)'
)

annotations = []
annotations2 = []

y_s = np.round(y_saving, decimals=2)
y_nw = np.round(y_net_worth, decimals=3)

# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x_saving):
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 4,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))

    # labeling the scatter savings
    annotations2.append(dict(xref='x1', yref='y1',
                             y=xd, x=ydn - 200000,
                             text='{:,}'.format(round(ydn, 3)),
                             font=dict(family='Arial', size=12,
                                       color='rgb(128, 0, 128)'),
                             showarrow=False))

# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=-0.2, y=-0.109,
                        text='Citibanamex ' +
                             '(2018), Cards Acquisition by Channels. ' +
                             '(Accessed on 11 July 2018)',
                        font=dict(family='Arial', size=10,
                                  color='rgb(150,150,150)'),
                        showarrow=False))


layout['annotations'] = annotations
layout2['annotations'] = annotations2

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H2('Cards Acquisitons'),
    html.H4('Horizontal Percentage Bars'),
    html.Div([
        html.H5('Household savings & net worth for eight OECD countries'),
        html.Div(
            className='four columns',
            children=dcc.Graph(id='cards-channels',
                               figure=go.Figure(data=data0,
                                                layout=layout)
                               )
        ),
        html.Div(
            className='four columns',
            children=dcc.Graph(id='cards-channels2',
                               figure=go.Figure(data=data1,
                                                layout=layout2)
                               )
        )
    ]),
])


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
