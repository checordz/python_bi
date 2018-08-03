from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime as dt

df = pd.read_csv('./CardsAquisition/ENTREGA_AL20JUN18_Limpia.csv')
df['FCH_ING'] = pd.to_datetime(df['FCH_ING'], format="%d/%m/%Y")
Products = {'AffinityCard': 1, 'AffinityCardZara': 2, 'BestBuyBanamex': 3, 'BestBuyMC': 4, 'BSMART': 5,
            'BSMARTCollage': 6, 'BSMARTFIRST': 7, 'CitiAAadvantageMC': 8, 'CitiPremiere': 9, 'CitiRewards': 10,
            'CitibankAAdvantageMC': 11, 'ClasicaMC': 12, 'clasicaMCinternacional': 13, 'Costco': 14,
            'MartiClasicaCitibanamex': 15, 'Marti_ClasicaCitibanamex': 16, 'MartiPremiumCitibanamex': 17,
            'Marti_PremiumCitibanamex': 18, 'OfficeDepotBanamex': 19, 'OroMastercard': 20, 'Platinum': 21,
            'Teleton': 22, 'TheHomeDepot': 23}







#####       Layout      ######

# app = dash.Dash()


# app.layout = html.Div(children=[
layout = html.Div(children=[
    html.H1(children='Bottom Funnel'),

    html.H3(children= 'Segment', className='mt-2'),

    html.Div([
        dcc.DatePickerRange(
            id='SegmentDatePickerRange',
            min_date_allowed=df['FCH_ING'].min(axis=0),
            max_date_allowed=df['FCH_ING'].max(axis=0),
            start_date=df['FCH_ING'].min(axis=0),
            end_date=df['FCH_ING'].max(axis=0),
        ),
        html.Div(id='SegmentBarDiv')
    ]),

    html.H3(children= 'Product Family', className='mt-2'),

    html.Div([
        dcc.DatePickerRange(
            id='ProductFamilyDatePickerRange',
            min_date_allowed=df['FCH_ING'].min(axis=0),
            max_date_allowed=df['FCH_ING'].max(axis=0),
            start_date=df['FCH_ING'].min(axis=0),
            end_date=df['FCH_ING'].max(axis=0),
        ),
        html.Div(id='ProductFamilyBarDiv')
    ]),

    html.H3(children='Product', className='mt-2'),

    html.Div([
        dcc.DatePickerRange(
            id='ProductDatePickerRange',
            min_date_allowed=df['FCH_ING'].min(axis=0),
            max_date_allowed=df['FCH_ING'].max(axis=0),
            start_date=df['FCH_ING'].min(axis=0),
            end_date=df['FCH_ING'].max(axis=0),
        ),
        html.Div(id='ProductBarDiv')
    ]),


], className='container-fluid')

##### Callback Segmento ######
@app.callback(
    dash.dependencies.Output('SegmentBarDiv', 'children'),
    [
        dash.dependencies.Input('SegmentDatePickerRange', 'start_date'),
        dash.dependencies.Input('SegmentDatePickerRange', 'end_date')
    ])
def UpdateSegmentGraph(start_date, end_date):
    #####       Segmento        #######

    traceSegmento = go.Bar(
        x=['ACC on Us', 'ACC off us', 'No hit', 'College', 'NTR', 'Rejected in PS1'],
        y=[df[(df['ESTRATEGY_DESC'] == 'ACC On Us') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'ACC Off Us') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'No Hit') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'College') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'NTR') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'Rejected in PS1') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__()],
        name='Completados',
        marker=dict(
            color='rgb(204,204,204)'
        )
    )
    trace2Segmento = go.Bar(
        x=['ACC on Us', 'ACC off us', 'No hit', 'College', 'NTR', 'Rejected in PS1'],
        y=[df[(df['ESTRATEGY_DESC'] == 'ACC On Us') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'ACC Off Us') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'No Hit') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'College') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'NTR') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['ESTRATEGY_DESC'] == 'Rejected in PS1') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__()],
        name='Booked',
        marker=dict(
            color='rgb(49,130,189)',
        )
    )

    trace3Segmento = go.Scatter(
        x=['ACC on Us', 'ACC off us', 'No hit', 'College', 'NTR', 'Rejected in PS1'],
        y=[(100 * trace2Segmento.y[0] / traceSegmento.y[0]), (100 * trace2Segmento.y[1] / traceSegmento.y[1]),
           (100 * trace2Segmento.y[2] / traceSegmento.y[2]), (100 * trace2Segmento.y[3] / traceSegmento.y[3]),
           (100 * trace2Segmento.y[4] / traceSegmento.y[4]), (100 * trace2Segmento.y[5] / traceSegmento.y[5])],
        name='%Booked',
        marker=dict(
            color='rgb(20,204,20)',
        ),
        yaxis='y2'
    )

    dataSegmento = [traceSegmento, trace2Segmento, trace3Segmento]

    layout = go.Layout(
        xaxis=dict(tickangle=-45),
        barmode='stack',
        yaxis=dict(
            title='Nominal Amount'
        ),
        yaxis2=dict(
            title='Percentage Amount',
            overlaying='y',
            side='right'
        ),
        paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'
    )
    SegmentGraph=dcc.Graph(
        id='SegmentBar',
        figure=go.Figure(
            data=dataSegmento,
            layout=layout
        )
    )
    return SegmentGraph
##### Callback Product Family ######
@app.callback(
    dash.dependencies.Output('ProductFamilyBarDiv', 'children'),
    [
        dash.dependencies.Input('ProductFamilyDatePickerRange', 'start_date'),
        dash.dependencies.Input('ProductFamilyDatePickerRange', 'end_date')
    ])
def UpdateProductFamilyGraph(start_date, end_date):
    ######      Familia     ######

    trace1Fam = go.Bar(
        x=['Bancarias', 'Coemitidas', 'Premium'],
        y=[df[(df['SEGMENTO'] == 'BANCARIAS') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['SEGMENTO'] == 'COEMITIDAS') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['SEGMENTO'] == 'PREMIUM') & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__()],
        name='Completados',
        marker=dict(
            color='rgb(204,204,204)'
        )
    )
    trace2Fam = go.Bar(
        x=['Bancarias', 'Coemitidas', 'Premium'],
        y=[df[(df['SEGMENTO'] == 'BANCARIAS') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['SEGMENTO'] == 'COEMITIDAS') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['SEGMENTO'] == 'PREMIUM') & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__()],
        name='Booked',
        marker=dict(
            color='rgb(49,130,189)',
        )
    )

    trace3Fam = go.Scatter(
        x=['Bancarias', 'Coemitidas', 'Premium'],
        y=[(100 * trace2Fam.y[0] / trace1Fam.y[0]), (100 * trace2Fam.y[1] / trace1Fam.y[1]),
           (100 * trace2Fam.y[2] / trace1Fam.y[2])],
        name='%Booked',
        marker=dict(
            color='rgb(20,204,20)',
        ),
        yaxis='y2'
    )

    dataFam = [trace1Fam, trace2Fam, trace3Fam]

    layoutFam = go.Layout(
        xaxis=dict(tickangle=-45),
        barmode='stack',
        yaxis=dict(
            title='Nominal Amount'
        ),
        yaxis2=dict(
            title='Percentage Amount',
            overlaying='y',
            side='right'
        ),
        paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'
    )

    ProductFamilyGraph=dcc.Graph(
        id='ProductFamily',
        figure=go.Figure(
            data=dataFam,
            layout=layoutFam
        )
    ),
    return ProductFamilyGraph

##### Callback Product ######
@app.callback(
    dash.dependencies.Output('ProductBarDiv', 'children'),
    [
        dash.dependencies.Input('ProductDatePickerRange', 'start_date'),
        dash.dependencies.Input('ProductDatePickerRange', 'end_date')
    ])
def UpdateProductGraph(start_date, end_date):
    #####       Producto    ######
    y = [df[(df['PRODUCTO_DESC'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 2) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 3) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 4) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 5) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 6) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 7) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 8) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 9) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 10) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 11) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 12) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 13) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 14) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 15) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 16) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 17) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 18) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 19) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 20) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 21) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 22) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         df[(df['PRODUCTO_DESC'] == 23) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
         ]



    trace1Prod = go.Bar(
        x=list(Products.keys()),
        y=[df[(df['PRODUCTO_DESC'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 2) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 3) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 4) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 5) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 6) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 7) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 8) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 9) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 10) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 11) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 12) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 13) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 14) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 15) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 16) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 17) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 18) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 19) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 20) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 21) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 22) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 23) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           ],
        name='Completados',
        marker=dict(
            color='rgb(204,204,204)'
        )
    )

    trace2Prod = go.Bar(
        x=list(Products.keys()),
        y=[df[(df['PRODUCTO_DESC'] == 1) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 2) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 3) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 4) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 5) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 6) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 7) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 8) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 9) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 10) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 11) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 12) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 13) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 14) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 15) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 16) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 17) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 18) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 19) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 20) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 21) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 22) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           df[(df['PRODUCTO_DESC'] == 23) & (df['Autenticado_vf'] == 1) & (df['Autenticado_vf'] == 1) & (df['FCH_ING'] <= end_date) & (df['FCH_ING'] >= start_date)].__len__(),
           ],
        name='Booked',
        marker=dict(
            color='rgb(49,130,189)',
        )
    )

    trace3Prod = go.Scatter(
        x=list(Products.keys()),
        y=[(100 * trace2Prod.y[0] / trace1Prod.y[0]), (100 * trace2Prod.y[1] / trace1Prod.y[1]),
           (100 * trace2Prod.y[2] / trace1Prod.y[2]), (100 * trace2Prod.y[3] / trace1Prod.y[3]),
           (100 * trace2Prod.y[4] / trace1Prod.y[4]), (100 * trace2Prod.y[5] / trace1Prod.y[5]),
           (100 * trace2Prod.y[6] / trace1Prod.y[6]), (100 * trace2Prod.y[7] / trace1Prod.y[7]),
           (100 * trace2Prod.y[8] / trace1Prod.y[8]), (100 * trace2Prod.y[9] / trace1Prod.y[9]),
           (100 * trace2Prod.y[10] / trace1Prod.y[10]), (100 * trace2Prod.y[11] / trace1Prod.y[11]),
           (100 * trace2Prod.y[12] / trace1Prod.y[12]), (100 * trace2Prod.y[13] / trace1Prod.y[13]),
           (100 * trace2Prod.y[14] / trace1Prod.y[14]), (100 * trace2Prod.y[15] / trace1Prod.y[15]),
           (100 * trace2Prod.y[16] / trace1Prod.y[16]), (100 * trace2Prod.y[17] / trace1Prod.y[17]),
           (100 * trace2Prod.y[18] / trace1Prod.y[18]), (100 * trace2Prod.y[19] / trace1Prod.y[19]),
           (100 * trace2Prod.y[20] / trace1Prod.y[20]), (100 * trace2Prod.y[21] / trace1Prod.y[21]),
           (100 * trace2Prod.y[22] / trace1Prod.y[22]),
           ],
        name='%Booked',
        marker=dict(
            color='rgb(20,204,20)',
        ),
        yaxis='y2'
    )

    dataProd = [trace1Prod, trace2Prod, trace3Prod]

    layoutProd = go.Layout(
        xaxis=dict(tickangle=-45),
        barmode='stack',
        yaxis=dict(
            title='Nominal Amount'
        ),
        yaxis2=dict(
            title='Percentage Amount',
            overlaying='y',
            side='right'
        ),
        paper_bgcolor='rgba(255,255,255,0)', plot_bgcolor='rgba(255,255,255,0)'
    )

    ProductGraph=dcc.Graph(
        id='Product',
        figure=go.Figure(
            data=dataProd,
            layout=layoutProd
        )
    )

    return ProductGraph


# if __name__ == '__main__':
#     app.run_server(debug=True)