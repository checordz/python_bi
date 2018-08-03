from app import app
# import graph
# from overview import overview, overview_digi
# from CitiPoC import client
from CardsAquisition import Vista1, Vista2
from CardsAcquisition_Funnel import funnel


import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64

encoded_image = base64.b64encode(open('./citibanamex_logo.svg', 'rb').read())

avatar_img = base64.b64encode(open('./avatar.png', 'rb').read())
login_div = html.Div([
    html.Div([
        html.Div([html.Img(src='data:image/png;base64,{}'.format(avatar_img.decode()), className='rounded mx-auto d-block')], id='avatar', className='form-group'),

        html.Div([
            dcc.Input(type='text', id='user', placeholder='Username', className='form-control')
        ], className='form-group'),
        html.Div([
            dcc.Input(type='password', id='pass', placeholder='Password', className='form-control')
        ], className='form-group'),
        html.Div([
            html.Button(children=['Login'], type='submit', id='login_button', className='btn btn-primary')
        ], className='form-group'),
        html.Div(id='alert_login', className='form-group')
    ], className='card rounded p-3 bg-light mx-auto d-block', style={'width':'25rem'})
], id='login-div', className='container')

main_div = html.Div([
    html.Button(children=['Dashboard'], type='submit', id='dashboard_button', className='btn btn-primary m-3', n_clicks_timestamp=1),
    html.Button(children=['Middle Funnel'], type='submit', id='middle_funnel_buttom', className='btn btn-primary m-3', n_clicks_timestamp=0),
    html.Button(children=['Bottom Funnel'], type='submit', id='bottom_funnel_button', className='btn btn-primary m-3', n_clicks_timestamp=0),
    html.Div(id='content', className='container-fluid mt-1')
])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([html.Img(src='data:image/svg+xml;base64,{}'.format(encoded_image.decode()))], id='logo', className='navbar navbar-expand bg-dark p-2'),
    html.Div(id='session', style={'display': 'none'}),
    login_div,
    html.Div(id='main-dv', className='container-fluid rounded bg-light'),
    html.Div(id='footer', className='navbar p-2')
], className='bg-dark')


@app.callback(Output('url','pathname'), [Input('dashboard_button','n_clicks_timestamp'), Input('middle_funnel_buttom','n_clicks_timestamp'), Input('bottom_funnel_button','n_clicks_timestamp')])
def change_url(want_dashboard, want_middle, want_bottom):
    print(want_dashboard)
    print(want_bottom)
    print(want_middle)
    if(want_dashboard > want_bottom and want_dashboard > want_middle):
        # print(n_clicks)
        return 'dashboard_page'
    if(want_bottom > want_dashboard and want_bottom > want_middle):
        return 'bottom_funnel_page'
    else:
        return 'middle_funnel_page'


@app.callback(Output('content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == 'dashboard_page':
        return Vista1.layout
    elif pathname == 'bottom_funnel_page':
        return Vista2.layout
    elif pathname == 'middle_funnel_page':
        return funnel.layout
    else:
        return None

@app.callback(Output('main-dv', 'children'), [Input('user', 'value'), Input('pass', 'value'), Input('login_button', 'n_clicks')])
def display_page(user, user_pass, n_clicks):
    if n_clicks and login(user, user_pass):
        return main_div
    else:
        return None



@app.callback(Output('login-div', 'style'), [Input('user', 'value'), Input('pass', 'value'), Input('login_button', 'n_clicks')])
def hide_login(user, user_pass, n_clicks):
    if n_clicks and login(user, user_pass):
        return {'display':'none'}

@app.callback(Output('alert_login', 'children'), [Input('user', 'value'), Input('pass', 'value'), Input('login_button', 'n_clicks')])
def show_login_error(user, user_pass, n_clicks):
    if n_clicks and login(user, user_pass) == False:
        return html.Div(children='Login failed: Incorrect combination of username/password', className='alert alert-danger')
    else:
        None

def login(username, password):
    # print(password)
    if username == 'bird' and password == 'bird':
        return True
    if username == 'panda' and password == 'panda':
        return True
    else:
        return False


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)