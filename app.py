######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['punch', 'body-slam', 'round-house kick to the face']
myheading='Chuck Norris execution method'
tabtitle='Chuck'
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

####### Layout of the app ########
app.layout = html.Div([
    html.H2(myheading),
    dcc.Dropdown(
        id='your-input-here',
        options=[{'label': i, 'value': i} for i in list_of_choices],
        value='punch'
    ),
    html.Div(id='your-output-here', children='')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'Chuck Norris will execute by {whatever_you_chose}'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
