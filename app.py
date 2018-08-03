import dash
import dash_html_components as html

app = dash.Dash()
server = app.server
app.config.suppress_callback_exceptions = True

app.scripts.config.serve_locally=True

app.head = [
    html.Title('Cards Acquisition')
]
app.css.append_css({
    'external_url': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css'
})

# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/dZVMbK.css"
# })