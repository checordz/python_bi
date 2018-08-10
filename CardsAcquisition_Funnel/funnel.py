from app import app
import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

# from __future__ import division

# # app = dash.Dash()
# server = app.server

colors1 = {
    'background': '#111111',
    'text': '#BEBEBE',
    'black': '#000000',
    'white': '#FFFFFF'
}

# campaign data
df = pd.read_csv('./CardsAcquisition_Funnel/funnel.csv')
df_fechas = pd.read_csv('./CardsAquisition/ENTREGA_AL20JUN18_Limpia.csv')
df_fechas['FCH_ING'] = pd.to_datetime(df_fechas['FCH_ING'], format="%d/%m/%Y")

# color for each segment
colors = ['#3973ac', '#993399', '#669900', '#b32d00', '#7300e6', '#cccc00']

cleaned_df = df.copy()


def clean_data(dataframe, value1):
    # some expensive clean data step
    cleaned_df = dataframe
    if '0' not in str(value1):
        cleaned_df['Affiliates'] = 0
        #print("Affiliates inactivo-----------------------------------------------------------------------------------")
    else:
        cleaned_df['Affiliates'] = df['Affiliates'].copy()
        #print("Affiliates activo--------------------------------------------------------------------------------------")
    if '1' not in str(value1):
        cleaned_df['Organic'] = 0
        #print("Organic inactivo---------------------------------------------------------------------------------------")
    else:
        cleaned_df['Organic'] = df['Organic'].copy()
        #print(
        #    "Organic activo-------------------------------------------------------------------------------------------")
    if '2' not in str(value1):
        cleaned_df['Search'] = 0
        #print(
        #    "Search inactivo------------------------------------------------------------------------------------------")
    else:
        cleaned_df['Search'] = df['Search'].copy()
        #print(
        #    "Search activo--------------------------------------------------------------------------------------------")
    if '3' not in str(value1):
        cleaned_df['X-Sell'] = 0
        #print(
        #    "X-Sell inactivo------------------------------------------------------------------------------------------")
    else:
        cleaned_df['X-Sell'] = df['X-Sell'].copy()
        #print(
        #    "X-Sell activo--------------------------------------------------------------------------------------------")
    if '4' not in str(value1):
        cleaned_df['Social'] = 0
        #print(
        #    "Social inactivo------------------------------------------------------------------------------------------")
    else:
        cleaned_df['Social'] = df['Social'].copy()
        #print(
        #    "Social activo--------------------------------------------------------------------------------------------")
    if '5' not in str(value1):
        cleaned_df['Display'] = 0
        #print(
        #    "Display inactivo-----------------------------------------------------------------------------------------")
    else:
        cleaned_df['Display'] = df['Display'].copy()
        #print(
        #    "Display activo-------------------------------------------------------------------------------------------")
    return cleaned_df


# print(cleaned_df)

# print(df)

def create_data_with_dataframe(cleaned_df):
    total_ch = [sum(row[1]) for row in cleaned_df.iterrows()]
    # print(total_ch)
    abs_perc = [total_ch[i] / total_ch[0] * 100 for i in range(1, total_ch.__len__())]
    abs_perc.insert(0, 100)
    # print(abs_perc)
    roundPerc_abs = [round(elem, 2) for elem in abs_perc]


    # rel_perc = [total_ch[i] / total_ch[i - 1] * 100 for i in range(1, total_ch.__len__())]
    rel_perc = []

    for index, channel in enumerate(total_ch):
        print(index)
        print(channel)
        print(total_ch[0])
        print(total_ch[2])
        if index < 3:
            rel_perc.append(channel / total_ch[0] * 100)
        else:
            rel_perc.append(channel / total_ch[2] * 100)

    # rel_perc.insert(0, 100)
    roundPerc_rel = [round(elem, 2) for elem in rel_perc]
    print(" lksdjfklajsd fklhasd fklsadfjkladjsf ")
    print(roundPerc_abs)
    print(" lksdjfklajsd fklhasd fklsadfjkladjsf ")
    print(roundPerc_rel)
    # paa cada callaback de box hacer un return con una variable booleana y un string dinamico y llamar a funcion que recicle codigos

    n_phase, n_seg = cleaned_df.shape

    plot_width = 600
    unit_width = plot_width / total_ch[0]

    phase_w = [int(value * unit_width) for value in total_ch]

    # height of a section and difference between sections
    section_h = 100
    section_d = 10

    # shapes of the plot
    shapes = []

    # plot traces data
    data = []

    # height of the phase labels
    label_y = []

    height = section_h * n_phase + section_d * (n_phase - 1)

    # rows of the DataFrame
    df_rows = list(cleaned_df.iterrows())

    # iteration over all the phases
    for i in range(n_phase):
        # phase name
        row_name = cleaned_df.index[i]

        # width of each segment (smaller rectangles) will be calculated
        # according to their contribution in the total users of phase
        seg_unit_width = phase_w[i] / total_ch[i]
        seg_w = [int(df_rows[i][1][j] * seg_unit_width) for j in range(n_seg)]

        # starting point of segment (the rectangle shape) on the X-axis
        xl = -1 * (phase_w[i] / 2)

        # iteration over all the segments
        for j in range(n_seg):
            # name of the segment
            seg_name = cleaned_df.columns[j]

            # corner points of a segment used in the SVG path
            points = [xl, height, xl + seg_w[j], height, xl + seg_w[j], height - section_h, xl, height - section_h]
            path = 'M {0} {1} L {2} {3} L {4} {5} L {6} {7} Z'.format(*points)

            shape = {
                'type': 'path',
                'path': path,
                'fillcolor': colors[j],
                'line': {
                    'width': 0.5,
                    'color': colors[j]
                }
            }
            shapes.append(shape)

            # to support hover on shapes
            hover_trace = go.Scatter(
                x=[xl + (seg_w[j] / 2)],
                y=[height - (section_h / 2)],
                hoverinfo='text+name',
                mode='markers',
                marker=dict(
                    size=2,  # min(seg_w[j] / 2, (section_h / 2)),
                    color=colors[j]
                ),
                text=" Segment: " + seg_name + ' ' + "<br>" + " Value: " + str(
                    "{:,}".format(cleaned_df[seg_name][row_name])) + ' ',
                name=' ' + str(round(cleaned_df[seg_name][row_name] / total_ch[i] * 100, 2)) + '% '
            )

            data.append(hover_trace)

            xl = xl + seg_w[j]

        # For phase values (total)
        value_trace = go.Scatter(
            x=[340] * n_phase,
            y=[height - (section_h / 2)],
            hoverinfo='text',
            mode='text',
            text='A: ' + str(roundPerc_abs[i]) + '%' + '<br>' + "R: " + str(roundPerc_rel[i]) + '%',
            showlegend=False,
            textfont=dict(
                # color='rgb(200,200,200)',
                size=15
            )
        )
        data.append(value_trace)

        # For phase names
        label_trace = go.Scatter(
            x=[-350] * n_phase,
            y=[height - (section_h / 2)],
            hoverinfo='text',
            mode='text',
            text=str(cleaned_df.index[i]) + '<br>' + str("{:,}".format(total_ch[i])),
            showlegend=False,
            textfont=dict(
                # color='rgb(200,200,200)',
                size=15
            )
        )
        data.append(label_trace)

        label_y.append(height - (section_h / 2))

        height = height - (section_h + section_d)

    return data, shapes


# app.layout = html.Div(style={'backgroundColor': 'rgba(9, 36, 71, 1)', 'color': colors1['text']}, children=[
layout = html.Div(children=[
    html.Div([
        html.H1('Middle Funnel')
    ], className = 'row'),
    html.Div([
        html.H6('Start Date - End Date:')
    ], className = 'row'),
    html.Div([
        dcc.DatePickerRange(
            id='MiddleFunnelDatePicker',
            min_date_allowed=df_fechas['FCH_ING'].min(axis=0),
            max_date_allowed=df_fechas['FCH_ING'].max(axis=0),
            start_date=df_fechas['FCH_ING'].min(axis=0),
            end_date=df_fechas['FCH_ING'].max(axis=0),
        ),
    ], className='row mb-2'),
    html.Div(children = [
            dcc.Dropdown(
                id='dropdown-menu',
                # className='container-fluid',
                options=[
                    {'label': 'Affiliates', 'value': 0},
                    {'label': 'Organic', 'value': 1},
                    {'label': 'Search', 'value': 2},
                    {'label': 'X-Sell', 'value': 3},
                    {'label': 'Social', 'value': 4},
                    {'label': 'Display', 'value': 5},
                ],
                value=[0, 1, 2, 3, 4, 5],
                multi=True
            ),
            # html.Div(id='category-output', className='six columns'),
        ], className = 'row'),
        html.Div(
            # className='eight columns',
            children=dcc.Graph(id='general-funnel')
        )
    ], className='container-fluid pb-5')


@app.callback(
    dash.dependencies.Output('general-funnel', 'figure'),
    [dash.dependencies.Input('dropdown-menu', 'value')])
def update_output(value):
    data, shapes = create_data_with_dataframe(clean_data(cleaned_df, value))
    # print('///////////////////////////////////////////////////////////////////////////////////////////////////////////')
    # print(cleaned_df)
    # print('/////////////////////////////////////////////////////////')
    # print(df)

    layout = go.Layout(
        # title="<b>Segmented Funnel Chart</b>",
        titlefont=dict(
            size=20,
            # color='rgb(230,230,230)'
        ),
        showlegend=False,
        hovermode='closest',
        shapes=shapes,
        # paper_bgcolor='rgba(9, 36, 71, 1)',
        # plot_bgcolor='rgba(9, 36, 71, 1)',
        paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)',
        xaxis=dict(
            showticklabels=False,
            zeroline=False,
            showline=False,
            showgrid=False,
        ),
        yaxis=dict(
            showticklabels=False,
            zeroline=False,
            showline=False,
            showgrid=False,
        ),
        margin=dict(
            l=30,
            r=30,
            t=50,
            b=50
        )
    )
    return go.Figure(data=data, layout=layout)


# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
# })

# if __name__ == '__main__':
#     app.run_server(debug=True)
