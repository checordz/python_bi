import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output, State
import base64

# app = dash.Dash()
#df_table = pd.read_csv('/Users/memomora/Coding/Python/bi_tool 2/CardsAcquisition_Funnel/funnel.csv')

trace1 = go.Bar(
    y=['Visits'],
    x=[20],
    width=[0.5],
    name='Started from Visits',
    orientation = 'h',
    marker = dict(
        color = 'rgba(68,126,182, 0.6)',
        line = dict(
            color = 'rgba(68,126,182, 1.0)',
            width = 3)
    )
)

trace2 = go.Bar(
    y=['Visits'],
    x=[12],
    width=[0.5],
    name='Completed from Started',
    orientation = 'h',
    marker = dict(
        color = 'rgba(253,134,63, 0.6)',
        line = dict(
            color = 'rgba(253,134,63, 1.0)',
            width = 3)
    )
)
trace3 = go.Bar(
    y=['Visits'],
    x=[6],
    width=[0.5],
    name='Approved from Completed',
    orientation = 'h',
    marker = dict(
        color = 'rgba(80,168,73, 0.6)',
        line = dict(
            color = 'rgba(80,168,73, 1.0)',
            width = 3)
    )
)

data = [trace3, trace2, trace1]

TableData = go.Table(
    header=dict(
        values=['Funnel Internet', '2018', 'Affiliates', 'Organic', 'Search', 'X-Sell', 'Social', 'Display'],
        fill = dict(color = 'rgba(68, 126, 182, 0.4)'),
        align=['center']
    ),
    cells=dict(
         values=[
             ['Visits', 'Start', 'Completed', 'Authenticated', 'Authorized Online', 'Delivered', 'Booked'],
             [3414072, 1336894, 425313, 256791, 55016, 34495, 33502],
             [1593452, 700838, 186528, 115887, 22890, 12091, 14118],
             [674844, 233190, 166754, 110383, 27481, 19211, 15154],
             [549130, 192956, 39260, 17979, 3341, 2413, 2554],
             [35919, 13971, 1308, 810, 171, 113, 1011],
             [503224, 185844, 30015, 11115, 1081, 628, 619],
             [57505, 10096, 1448, 617, 52, 39, 46],

         ],
        #values=[df_table[k].tolist() for k in df_table.columns[1:]],
        format=[None] + [", .2f"] * 2,
        align=['center']
    ),
    columnwidth=[18,10]
)

Pielabels=['Affiliates', 'Organic', 'Search', 'XSell', 'Social', 'Display']

Started = go.Pie(opacity=0.85,
                     labels=Pielabels,
                     values=[700, 233, 192, 13, 185, 10],
                     hole=0.3,
                     pull=0.15,
                     marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                        'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                             'line': dict(width=0)},
                     hoverinfo='label+value',
                     textinfo='percent',
                     textfont=dict(color='black')
             )
Conversion = go.Pie(opacity=0.95,
                        labels=Pielabels,
                        values=[186, 166, 39, 10, 30, 10],
                        hole=0.3,
                        pull=0.15,
                        marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                           'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                                'line': dict(width=0)},
                        hoverinfo='label+value',
                        textinfo='percent',
                        textfont=dict(color='black')
               )
Authenticated = go.Pie(opacity=0.95,
                       labels=Pielabels,
                       values=[115, 110, 18, 1, 11, 617],
                       hole=0.3,
                       pull=0.15,
                       marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                          'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                               'line': dict(width=0)},
                       hoverinfo='label+value',
                       textinfo='percent',
                       textfont=dict(color='black')

               )
ApprovalOnline = go.Pie(opacity=0.95,
                            labels=Pielabels,
                            values=[22,27,3,0.2,1,0.05],
                            hole=0.3,
                            pull=0.15,
                            marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                               'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                                    'line': dict(width=0)},
                            hoverinfo='label+value',
                            textinfo='percent',
                            textfont=dict(color='black')

                            )

Delivered = go.Pie(opacity=0.95,
                            labels=Pielabels,
                            values=[12,19,2.4,1,0.63,0.04],
                            hole=0.3,
                            pull=0.15,
                            marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                               'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                                    'line': dict(width=0)},
                            hoverinfo='label+value',
                            textinfo='percent',
                            textfont=dict(color='black')

                            )

Booked = go.Pie(opacity=0.95,
                            labels=Pielabels,
                            values=[14.1,15.1,2.5,1.01,0.6,0.046],
                            hole=0.3,
                            pull=0.15,
                            marker={'colors': ['rgb(68,126,182)', 'rgb(253,134,63)', 'rgb(80,168,73)',
                                               'rgb(215,65,70)', 'rgb(153,111,191)', 'rgb(145,99,92)'],
                                    'line': dict(width=0)},
                            hoverinfo='label+value',
                            textinfo='percent',
                            textfont=dict(color='black')

                            )

PieData = [Started, Conversion, Authenticated, ApprovalOnline, Delivered, Booked]

# app.layout = html.Div(children=[
layout = html.Div(children=[
    html.H1('Cards Acquisition - General Dashboard'),
    html.Div([
        html.Div(
            className='row',
            children=dcc.Graph(id='InfoBar',
                               figure=go.Figure(data=data,
                                                layout=go.Layout(barmode='stack',
                                                                 xaxis=dict(
                                                                     showgrid=False,
                                                                     showline=False,
                                                                     showticklabels=False,
                                                                     zeroline=True,
                                                                 ),
                                                                 hovermode='closest',
                                                                 margin={'l':50,
                                                                         'b':50,
                                                                         'r':0,
                                                                         't':100},
                                                               paper_bgcolor='rgba(255,255,255,0)',
                                                                plot_bgcolor='rgba(255,255,255,0)'
                                                                 )
                                                ),
                               # style={'width': 1000, 'height':250},
                               style={'height':250, 'width':'100%'},

                               )
        ),
    html.Div([
        html.Div(
            className='col',
            children=dcc.Graph(id='Start',
                               figure=go.Figure(data=[PieData[0]],
                                                layout=go.Layout(title="<b>Started</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                               )
        ),
        html.Div(
            className='col',
            children=dcc.Graph(id='Conv',
                               figure=go.Figure(data=[PieData[1]],
                                                layout=go.Layout(title="<b>Conversion</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                               )
        )
    ], className='row'),

    html.Div([
        html.Div(
            className='col',
            children=dcc.Graph(id='Auth',
                               figure=go.Figure(data=[PieData[2]],
                                                layout=go.Layout(title="<b>Authenticated</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                               )
        ),
        html.Div(
            className='col',
            children=dcc.Graph(id='Approv',
                               figure=go.Figure(data=[PieData[3]],
                                                layout=go.Layout(title="<b>Approval Online</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                               )
        )
    ], className='row'),

    html.Div([
        html.Div(
            className='col',
            children=dcc.Graph(id='Delivered',
                                figure=go.Figure(data=[PieData[4]],
                                                layout=go.Layout(title="<b>Delivered</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                                )
        ),
        html.Div(
            className='col',
            children=dcc.Graph(id='Booked',
                                figure=go.Figure(data=[PieData[5]],
                                                layout=go.Layout(title="<b>Booked</b>", paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'),

                                                )
                                )
        )
    ], className='row'),



    html.Div(
        className='row',
        children = html.Div(
            children = dcc.Graph(id='InfoTable',
                    figure=go.Figure(data=[TableData],
                        layout=go.Layout(paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)')
                    ),
                # style={'width': 300}
            ),
            className = 'col')
    ),
]),


], className='container-fluid')

# @app.callback(
#     Output(component_id='my-div', component_property='children'),
#     [Input(component_id='my-id', component_property='value')]
# )
# def update_output_div(input_value):
#     return 'You\'ve entered "{}"'.format(input_value)

# app.css.append_css({
#     'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
# })

# if __name__ == '__main__':
#     app.run_server()