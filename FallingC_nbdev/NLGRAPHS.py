# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 01:09:43 2022

@author: lnico
"""

def individualpos(df1, df2, driver):
    
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np
    
    fig = make_subplots(rows=3, cols=2, row_heights=[0.1, 0.45, 0.45],shared_xaxes=True,vertical_spacing=0.03, horizontal_spacing = 0.03, subplot_titles=("Dark phase", "Light phase", "", " "))

    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=1)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=1)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="#7f7f7f",row=1,col=1)
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=2)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=2)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="green",row=1,col=2)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=1)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=1)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=2)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=2)
    
    time = df1.loc[df1.ExperimentState == "Dark", 'Seconds']
    #wt_dark
    for n in df1.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df1[(df1["ExperimentState"] == "Dark")].loc[:,n],
            mode='lines',
            name='Y Position (mm)'
        ), row=2, col=1)
    
    #wt_light
    for n in df1.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df1[(df1["ExperimentState"] == "Full")].loc[:,n],
            mode='lines',
            name='Y Position (mm)'
        ), row=2, col=2)
        
    #Expt_dark    
    for n in df2.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df2[(df2["ExperimentState"] == "Dark")].loc[:,n],
            mode='lines',
            name='Y Position (mm)'
        ), row=3, col=1)
        
    #expt_light    
    for n in df2.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df2[(df2["ExperimentState"] == "Full")].loc[:,n],
            mode='lines',
            name='Y Position (mm)'
        ), row=3, col=2)

    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=3,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=2)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=3,col=2)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,20,5),row=3,col=1)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,20,5),row=3,col=2)
    fig.update_yaxes(title='Y position (mm)_wt',range=[0,90],tickvals=np.arange(0,91,20),row=2,col=1)
    fig.update_yaxes(range=[0,90],row=2,col=2)
    fig.update_yaxes(range=[0,90],row=3,col=2)
    fig.update_yaxes(title='Y position (mm)_expt',range=[0,90],tickvals=np.arange(0,91,20),row=3,col=1)
    fig.update_layout(title = driver + "      Mean of Y position(mm)", font=dict(family="ibm plex sans",size=14,),height=800, width=1200, hovermode='x unified', showlegend=False)
    
    return fig

def yposmean(df3, df4, driver):
    
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np
    
    fig = make_subplots(rows=2, cols=2, row_heights=[0.1, 0.85],shared_xaxes=True,vertical_spacing=0.03, horizontal_spacing = 0.03, subplot_titles=("Dark phase", "Light phase", "", " "))
    
    #basic cartoon
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=1)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=1)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="#7f7f7f",row=1,col=1)
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=2)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=2)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="green",row=1,col=2)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=1)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=1)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=2)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=2)
    
    time = df3.loc[df3.ExperimentState == "Dark", 'Seconds']
    #expt_dark
    fig.append_trace(go.Scattergl(x =time,
            y=df3.loc[df3.ExperimentState == "Dark", 'mean'],
            mode='lines',
            name='Mean of Y position(mm)_Expt',
            marker = dict(color = "#15B01A"),
            line=dict(width=2),
            showlegend=True    
        ), row=2, col=1)
    
    #expt_light
    fig.append_trace(go.Scattergl(x =time,
            y=df3.loc[df3.ExperimentState == "Full", 'mean'],
            mode='lines',
            name='Mean of Y position(mm)_Expt',
            marker = dict(color = "#15B01A"),
            line=dict(width=2),
            showlegend=False    
        ), row=2, col=2)
    
    #exptdark_CI
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Dark", 'mean']+df3.loc[df3.ExperimentState == "Dark", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=1)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Dark", 'mean']-df3.loc[df3.ExperimentState == "Dark", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=1)
    
    #exptlight_CI
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Full", 'mean']+df3.loc[df3.ExperimentState == "Full", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=2)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Full", 'mean']-df3.loc[df3.ExperimentState == "Full", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=2)
    
    #wt dark mean
    fig.append_trace(go.Scattergl(x =time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean'],
            mode='lines',
            name='Mean of Y position(mm)_WT',
            marker = dict(color = "#000"),
            line=dict(width=2),
            showlegend=True                              
        ), row=2, col=1)
    
    #wt light mean
    fig.append_trace(go.Scattergl(x =time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean'],
            mode='lines',
            name='Mean of Y position(mm)_WT',
            marker = dict(color = "#000"),
            line=dict(width=2),
            showlegend=False        
        ), row=2, col=2)
    
    #wtdarkCI
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean']+df4.loc[df4.ExperimentState == "Dark", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=1)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean']-df4.loc[df4.ExperimentState == "Dark", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=1)
    
    #wtlightCI
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean']+df4.loc[df4.ExperimentState == "Dark", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=2)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean']-df4.loc[df4.ExperimentState == "Dark", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=2)
    
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=90,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=2)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,21,5),row=2,col=1)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,21,5),row=2,col=2)
    fig.update_yaxes(title='Y position (mm)',range=[0,90],tickvals=np.arange(0,91,20),row=2,col=1)
    fig.update_yaxes(range=[0,90],tickvals=np.arange(0,91,20),row=2,col=2)
    fig.update_yaxes(range=[0,90],row=2,col=2)
    fig.update_yaxes(title='Mean of Y position (mm)',range=[0,90],tickvals=np.arange(0,91,20),row=2,col=1)
    fig.update_layout(title = driver + "      Mean of Y position(mm)", font=dict(family="ibm plex sans",size=14,),height=600, width=1200, hovermode='x unified', showlegend=True)
    
    return fig
 
def individualspeed(df1,df2, driver):
    
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np
    
    fig = make_subplots(rows=3, cols=2, row_heights=[0.1, 0.45, 0.45],shared_xaxes=True,vertical_spacing=0.03, horizontal_spacing = 0.03, subplot_titles=("Dark phase", "Light phase", "", " "))
    
    #basic cartoon
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=1)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=1)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="#7f7f7f",row=1,col=1)
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=2)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=2)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="green",row=1,col=2)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=1)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=1)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=2)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=2)
    
    
    time = df1.loc[df1.ExperimentState == "Dark", 'Seconds']
    #individual lines (wt)
    for n in df1.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df1[(df1["ExperimentState"] == "Dark")].loc[:,n],
            mode='lines',
            name='Speed (mm/s)'
        ), row=2, col=1)
        
    for n in df1.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df1[(df1["ExperimentState"] == "Full")].loc[:,n],
            mode='lines',
            name='Speed (mm/s)'
        ), row=2, col=2)
        
    #individual lines (expt)
    for n in df2.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df2[(df2["ExperimentState"] == "Dark")].loc[:,n],
            mode='lines',
            name='Speed (mm/s)'
        ), row=3, col=1)
        
    for n in df2.columns[2:]:
        fig.append_trace(go.Scattergl(x =time,
            y=df2[(df2["ExperimentState"] == "Full")].loc[:,n],
            mode='lines',
            name='Speed (mm/s)'
        ), row=3, col=2)
            

    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=3,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=3,col=2)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=2)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,21,5),row=3,col=1)
    fig.update_xaxes(title='Seconds(s)', range=[0,20],tickvals=np.arange(0,21,5),row=3,col=2)
    fig.update_yaxes(title= 'Speed (mm/s)_WT',range=[0,100],tickvals=np.arange(0,101,20),row=2,col=1)
    fig.update_yaxes(range=[0,100],tickvals=np.arange(0,101,20),row=2,col=2)
    fig.update_yaxes(title='Speed (mm/s)_EXPT',range=[0,100],tickvals=np.arange(0,101,20),row=3,col=1)
    fig.update_yaxes(range=[0,100],tickvals=np.arange(0,101,20),row=3,col=2)
    fig.update_layout(title = driver + "      Mean of Speed (mm/s)", font=dict(family="ibm plex sans",size=14,),height=600, width=1200, hovermode='x unified', showlegend=False)
    
    return fig

def speedmeangraph(df3, df4,driver):
    
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np

    fig = make_subplots(rows=2, cols=2, row_heights=[0.1, 0.85],shared_xaxes=True,vertical_spacing=0.03, horizontal_spacing = 0.03, subplot_titles=("Dark phase", "Light phase", "", " "))
    
    #basic cartoon
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=1)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=1)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="#7f7f7f",row=1,col=1)
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=2)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=2)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="green",row=1,col=2)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=1)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=1)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=2)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=2)
    
    time = df3.loc[df3.ExperimentState == "Dark", 'Seconds']
    #exptdark
    fig.append_trace(go.Scattergl(x =time,
            y=df3.loc[df3.ExperimentState == "Dark", 'mean'],
            mode='lines',
            name='Mean speed (mm/s)_Expt',
            marker = dict(color = "#15B01A"),
            line=dict(width=2),
            showlegend=True    
        ), row=2, col=1)
    
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Dark", 'mean']+df3.loc[df3.ExperimentState == "Dark", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=1)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=df3['Seconds'],
            y=df3.loc[df3.ExperimentState == "Dark", 'mean']-df3.loc[df3.ExperimentState == "Dark", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=1)
    
    #exptlight
    fig.append_trace(go.Scattergl(x =(df3['Seconds']),
            y=df3.loc[df3.ExperimentState == "Full", 'mean'],
            mode='lines',
            name='Mean speed (mm/s)_Expt',
            marker = dict(color = "#15B01A"),
            line=dict(width=2),
            showlegend=False    
        ), row=2, col=2)
    
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df3.loc[df4.ExperimentState == "Full", 'mean']+df3.loc[df3.ExperimentState == "Full", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=2)
    
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df3.loc[df3.ExperimentState == "Full", 'mean']-df3.loc[df3.ExperimentState == "Full", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=2)
    
    
    #wtdark
    fig.append_trace(go.Scattergl(x =time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean'],
            mode='lines',
            name='Mean speed (mm/s)_WT',
            marker = dict(color = "#000"),
            line=dict(width=2),
            showlegend=True    
        ), row=2, col=1)
    
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean']+df4.loc[df4.ExperimentState == "Dark", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=1)
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Dark", 'mean']-df4.loc[df4.ExperimentState == "Dark", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=1)
    
    #wtlight
    fig.append_trace(go.Scattergl(x =time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean'],
            mode='lines',
            name='Mean speed (mm/s)_WT',
            marker = dict(color = "#000"),
            line=dict(width=2),
            showlegend=False    
        ), row=2, col=2)
    
    fig.append_trace(go.Scatter(
            name='Upper Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean']+df4.loc[df4.ExperimentState == "Full", 'CI'],
            mode='lines',
            marker=dict(color="#444"),
            line=dict(width=0),
            showlegend=False
        ), row=2, col=2)
    
    fig.append_trace(go.Scatter(
            name='Lower Bound',
            x=time,
            y=df4.loc[df4.ExperimentState == "Full", 'mean']-df4.loc[df4.ExperimentState == "Full", 'CI'],
            marker=dict(color="#444"),
            line=dict(width=0),
            mode='lines',
            fillcolor='rgba(68, 68, 68, 0.3)',
            fill='tonexty',
            showlegend=False
        ), row=2, col=2)
    
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=1)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=100,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=2)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,21,5),row=2,col=1)
    fig.update_xaxes(title='Seconds(s)',range=[0,20],tickvals=np.arange(0,21,5),row=2,col=2)
    fig.update_yaxes(title='Mean of Speed (mm/s)',range=[0,30],tickvals=np.arange(0,31,5),row=2,col=1)
    fig.update_yaxes(range=[0,30],tickvals=np.arange(0,31,5),row=2,col=2)
    fig.update_layout(title = driver + "      Mean of Speed (mm/s)", font=dict(family="ibm plex sans",size=14,),height=800, width=1400, hovermode='x unified', showlegend=True)
    
    return fig       

def fallingraph(df1, df2, df3, df4, df5, df6, df7, df8, driver, showpos = True):
    #if showpos = True, plots the additional y position curves for WT and expt
    #if showpos = False, ignores the ypos curves
    
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np
    
    fig = make_subplots(rows=2, cols=2, row_heights=[0.1, 0.85],shared_xaxes=True,vertical_spacing=0.03, horizontal_spacing = 0.03, subplot_titles=("Dark phase", "Light phase", "", " "), specs=[[{},{}], [{"secondary_y": True}, {"secondary_y": True}]])

    #basic cartoon
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=1)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=1)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="#7f7f7f",row=1,col=1)
    fig.add_trace(go.Scatter(x=[], y=[]),row=1, col=2)
    fig.add_shape(type="rect",x0=0, y0=0, x1=3, y1=1,line=dict(color="black",width=2,),fillcolor="black",row=1,col=2)
    fig.add_shape(type="rect",x0=3, y0=0, x1=23, y1=1,line=dict(color="black",width=2,),fillcolor="green",row=1,col=2)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=1)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=1)
    fig.update_xaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,20.05],row=1, col=2)
    fig.update_yaxes(showgrid=False,zeroline=False,ticks="",showline=False,showticklabels=False,range=[-0.05,1.05],row=1, col=2)
    
    #falling
    #WTdark
    for n in df1.columns[0:]:
        fig.add_trace(go.Bar(
            x=df1['Seconds'],
            y=df1['Total falls per sec'],        
            name='Falling occurence_WT', 
            marker=dict(
            color='rgba(192,192,192,0.5)',
            line=dict(width=0)),
            showlegend = False
        ), row =2, col = 1, secondary_y = False)
        
    #WTlight
    for n in df2.columns[0:]:
        fig.add_trace(go.Bar(
            x=df1['Seconds'],
            y=df2['Total falls per sec'],       
            name='Falling occurence_WT',  
            marker=dict(
            color='rgba(192,192,192,0.5)',
            line=dict(width=0)),
            showlegend = False
        ), row =2, col = 2, secondary_y = False)
    
    
    #EXPTdark
    for n in df3.columns[0:]:
        fig.add_trace(go.Bar(
            x=df3['Seconds'],
            y=df3['Total falls per sec'], width = 0.05,       
            name='Falling occurence_Expt', 
            marker=dict(
            color='rgba(0,100,0,1)', 
            line=dict(width=0),
            opacity=0.6),
            showlegend = False
        ), row =2, col = 1, secondary_y = False)
        
    #EXPTlight
    for n in df4.columns[0:]:
        fig.add_trace(go.Bar(
            x=df3['Seconds'],
            y=df4['Total falls per sec'], width = 0.05,        
            name='Falling occurence_Expt',  
            marker=dict(
            color='rgba(0,100,0,1)', 
            line=dict(width=0),
            opacity = 0.2),
            showlegend = False
        ), row =2, col = 2, secondary_y = False)
        
    if showpos == True:
        #y position
        #expt_dark
        fig.add_trace(go.Scattergl(x =(df5['Seconds']),
                y=df5['mean'],
                mode='lines',
                name='Mean of Y position(mm)_Expt',
                marker = dict(color = "#15B01A"),
                line=dict(width=2),
                showlegend=False    
            ), row=2, col=1, secondary_y = True)
        
        #expt_light
        fig.add_trace(go.Scattergl(x =(df5['Seconds']),
                y=df6['mean'],
                mode='lines',
                name='Mean of Y position(mm)_Expt',
                marker = dict(color = "#15B01A"),
                line=dict(width=2),
                showlegend=False    
            ), row=2, col=2, secondary_y = True)
        
        #exptdark_CI
        fig.add_trace(go.Scatter(
                name='Upper Bound',
                x=df5['Seconds'],
                y=df5['mean']+df5['CI'],
                mode='lines',
                marker=dict(color="#444"),
                line=dict(width=0),
                showlegend=False
            ), row=2, col=1, secondary_y = True)
        fig.add_trace(go.Scatter(
                name='Lower Bound',
                x=df5['Seconds'],
                y=df5['mean']-df5['CI'],
                marker=dict(color="#444"),
                line=dict(width=0),
                mode='lines',
                fillcolor='rgba(68, 68, 68, 0.3)',
                fill='tonexty',
                showlegend=False
            ), row=2, col=1, secondary_y = True)
        
        #exptlight_CI
        fig.add_trace(go.Scatter(
                name='Upper Bound',
                x=df5['Seconds'],
                y=df6['mean']+df6['CI'],
                mode='lines',
                marker=dict(color="#444"),
                line=dict(width=0),
                showlegend=False
            ), row=2, col=2, secondary_y = True)
        fig.add_trace(go.Scatter(
                name='Lower Bound',
                x=df5['Seconds'],
                y=df6['mean']-df6['CI'],
                marker=dict(color="#444"),
                line=dict(width=0),
                mode='lines',
                fillcolor='rgba(68, 68, 68, 0.3)',
                fill='tonexty',
                showlegend=False
            ), row=2, col=2, secondary_y = True)
        
        #wt dark mean
        fig.add_trace(go.Scattergl(x =(df7['Seconds']),
                y=df7['mean'],
                mode='lines',
                name='Mean of Y position(mm)_WT',
                marker = dict(color = "#000"),
                line=dict(width=2),
                showlegend=False                              
            ), row=2, col=1, secondary_y = True)
        
        #wt light mean
        fig.add_trace(go.Scattergl(x =(df7['Seconds']),
                y=df8['mean'],
                mode='lines',
                name='Mean of Y position(mm)_WT',
                marker = dict(color = "#000"),
                line=dict(width=2),
                showlegend=False        
            ), row=2, col=2, secondary_y = True)
        
        #wtdarkCI
        fig.add_trace(go.Scatter(
                name='Upper Bound',
                x=df7['Seconds'],
                y=df7['mean']+df7['CI'],
                mode='lines',
                marker=dict(color="#444"),
                line=dict(width=0),
                showlegend=False
            ), row=2, col=1, secondary_y = True)
        fig.add_trace(go.Scatter(
                name='Lower Bound',
                x=df7['Seconds'],
                y=df7['mean']-df7['CI'],
                marker=dict(color="#444"),
                line=dict(width=0),
                mode='lines',
                fillcolor='rgba(68, 68, 68, 0.3)',
                fill='tonexty',
                showlegend=False
            ), row=2, col=1, secondary_y = True)
        
        #wtlightCI
        fig.add_trace(go.Scatter(
                name='Upper Bound',
                x=df7['Seconds'],
                y=df8['mean']+df8['CI'],
                mode='lines',
                marker=dict(color="#444"),
                line=dict(width=0),
                showlegend=False
            ), row=2, col=2, secondary_y = True)
        fig.add_trace(go.Scatter(
                name='Lower Bound',
                x=df7['Seconds'],
                y=df8['mean']-df8['CI'],
                marker=dict(color="#444"),
                line=dict(width=0),
                mode='lines',
                fillcolor='rgba(68, 68, 68, 0.3)',
                fill='tonexty',
                showlegend=False
            ), row=2, col=2, secondary_y = True)
    
        
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=60,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=1, secondary_y = False)
    fig.add_shape(type="line",x0=3, y0=0, x1=3, y1=60,line=dict(color="black",width=3,dash = "dot"),fillcolor="black", row=2,col=2, secondary_y = False)
    
    fig.update_yaxes(title='Falling occurence',title_font=dict(size=20), range=[0,15],tickvals=np.arange(0,16,2),row=2,col=1, secondary_y = False)
    fig.update_yaxes(title='Mean of Y position(mm)',title_font=dict(size=20), range=[0,15],tickvals=np.arange(0,16,2),row=2,col=2, secondary_y = True)
    
    
    fig.update_yaxes(range=[0,1],tickvals=np.arange(0,1,0.1),row=2,col=1, secondary_y = False)
    fig.update_yaxes(range=[0,1],tickvals=np.arange(0,1,0.1),row=2,col=2, showticklabels=False, secondary_y = False)
    fig.update_yaxes(range=[0,90],tickvals=np.arange(0,91,9),row=2,col=1, showticklabels=False, secondary_y = True)
    fig.update_yaxes(range=[0,90],tickvals=np.arange(0,91,9),row=2,col=2, secondary_y = True)
    
    fig.update_xaxes(title='Seconds(s)',title_font=dict(size=20), range=[0,20],tickvals=np.arange(0,21,5),row=2,col=1)
    fig.update_xaxes(title='Seconds(s)',title_font=dict(size=20), range=[0,20],tickvals=np.arange(0,21,5),row=2,col=2)
    fig.update_layout(title = driver + "      Falling Occurence", font=dict(family="ibm plex sans",size=14,),height=800, width=1800, hovermode='x unified', showlegend=False, barmode = 'overlay')
    
    return fig

def violinfallgraph(df1, df2, df3, df4, driver):
    import plotly.graph_objects as go
    import numpy as np
    
    fig = go.Figure()


    fig.add_trace(go.Violin(x = df1['ExperimentState'],
                            y=df1['value'],                        
                            legendgroup='WT', scalegroup='WT', name='WT_Dark',
                            side='negative', # where to position points
                            pointpos = -0.7,
                            line_color='gray'))
    
    fig.add_trace(go.Violin(x = df2['ExperimentState'],
                            y=df2['value'],
                            legendgroup='Expt_Dark', scalegroup='Expt_Dark', name='Expt_Dark',
                            side='positive',
                            pointpos = 0.9,
                            line_color='lightseagreen'))
    
    
    fig.add_trace(go.Violin(x = df3['ExperimentState'],
                            y=df3['value'],                        
                            legendgroup='WT', scalegroup='WT', name='WT_Full',
                            side='negative', # where to position points
                            pointpos = -0.7,
                            line_color='gray'))
    
    fig.add_trace(go.Violin(x = df4['ExperimentState'],
                            y=df4['value'],
                            legendgroup='Expt', scalegroup='Expt', name='Expt_Full',
                            side='positive',
                            pointpos = 0.7,
                            line_color='lightseagreen'))
    
    # update characteristics shared by all traces
    fig.update_traces(meanline_visible=True,
                      points='all', # show all points
                      jitter=0.05,  # add some jitter on points for better visibility
                      scalemode='count') #scale violin plot area with total count
    
    fig.update_yaxes(title='Second(s)',title_font=dict(size=20), range=[-10,30],tickvals=np.arange(-10,31,5))
    fig.update_xaxes(title='Phase',title_font=dict(size=20))
    fig.update_layout(title = driver + "      Distribution of Falls", font=dict(family="ibm plex sans",size=14,),height=800, width=1700, hovermode='x unified', showlegend=False, violingap=0, violinmode='overlay')
    
    return fig