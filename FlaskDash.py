#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import flask
from flask import render_template
from dash.dependencies import Input, Output


# In[ ]:


server = flask.Flask(__name__)

@server.route('/')
def index():
    return render_template('Index.html')

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div(className='container',children=[
    html.Div(className='row align-items-center min-vh-100' ,
            children=[
                html.Div(className='col-3',children=[
                            html.P('Here'),
                            html.Br(),
                            dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018}],
                 multi=False,
                 value=2015,
                 style={'width':'92%'}
                                         
                 )
                            
                        ]
                        ),
                html.Div(className='col-9',children=[
                            html.Div(id='output_container', children=[],style={'text-align':'center'}),
                            dcc.Graph(id='graph-bar',figure={})
                        ]                   
                        )
            ])
    
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='graph-bar', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)
    x = ['January','February','March']
    y = [10,20,15]
    x1= ['April','May','June']
    y2 = [110,120,98]
    if option_slctd == 2015:
        trace = go.Bar(
        x = x,
        y = y
        )
    else:
        trace = go.Bar(
        x = x1,
        y = y2
        )
    data = [trace]
    fig = go.Figure(data=data)
   

    return container, fig

if __name__ == '__main__':
    app.run_server()


# In[ ]:




