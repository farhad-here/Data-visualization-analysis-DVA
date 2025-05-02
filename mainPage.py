#Libraries
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from matplotlib import pyplot as plt
import streamlit as st
from bokeh.plotting import figure
import altair as alt
import plotly.express as px
#======================================
#for my page layout in streamlit
st.set_page_config(layout='wide')
#=======================================
#name
'# DVA (Data visualization analysis)'
'##### made by Farhad Ghaherdoost'
#=======================================
#upload file
st.info('format .xlsx or .csv')
vorodi = st.file_uploader('Data')
'-----------------------------'
#=======================================
# for csv
if vorodi != None:
    if '.csv' in vorodi.name:
        #read file
        df = pd.read_csv(vorodi)
        #columns for vector
        col_list = list(df.columns)
        #sort values
        check_sort = st.checkbox('Sort Values')
        if check_sort == True:
            select_box_sort = st.selectbox('what do you want for x',col_list,key='select_box_clean')
            df = df.sort_values(by=[select_box_sort], ignore_index=True,ascending=True)
            show_data = st.button('Show Data')
            if show_data == True:
                st.write(df)
        #select box
        '---------------'
        select_box = st.selectbox('what do you want for x',col_list)
        select_box_2 = st.selectbox('what do you want for y',col_list)

        #line chart for selectbox
        st.line_chart(df,x=select_box,y=select_box_2)
        '---------------------'
        #select chart and column you want
        charts = st.selectbox('what kind of chart you want?',['boxplot','areachart','barchart','bokeh','altairchart','scatter','linechart'])
        select_box_3 = st.selectbox('what do you need for x',col_list)
        select_col = st.selectbox('what you need for y',col_list)
        #all kind of charts
        if charts == 'areachart':
            st.area_chart(df, x=select_box_3, y=select_col)
        elif charts == 'barchart':
            st.bar_chart(df, x=select_box_3, y=select_col)
        elif charts == 'bokeh':
            p = figure(
                title='simple line example',
                x_axis_label=select_box_3,
                y_axis_label=select_col)
            p.line(df[select_box_3], df[select_box_3], legend_label='Trend', line_width=2)
            st.bokeh_chart(p, use_container_width=True)  
        elif charts == 'altairchart':
            c = (
            alt.Chart(df)
            .mark_circle()
            .encode(x=select_box_3, y=select_col)
            )

            st.altair_chart(c, use_container_width=True)
        elif charts == 'scatter':
            st.scatter_chart(
                    df,
                    x=select_box_3,
                    y=select_col
                )
        elif charts == 'linechart':
                st.line_chart(df, x=select_box_3, y=select_col)
        elif charts == 'boxplot':
                fig = px.box(df, x=select_box_3, y=select_col)
                st.plotly_chart(fig, theme=None, use_container_width=True)

        '---------------------'
        '### everything you want just select it'
        #select what you wanna know
        #columns grid
        #checked be in here
        col_chart = []
        #creat in number of columns->checkbox for it
        select_box_4 = st.selectbox('select your x',col_list)
        col_1,col_2 = st.columns(2)
        for i in col_list:
            check = col_1.checkbox(i)
            if check == True:
                col_chart.append(i)
        #show in plot
        for i in col_chart:
            col_2.line_chart(df,x=select_box_4,y=i,height=500,width=700)
        '----------------------'
    
        '### select what chart and what column or columns you want to see'
        #select chart
        select_box_5 = st.selectbox('x',col_list)
        char = st.selectbox('chart',['boxplot1','boxplot2','areachart','barchart','bokeh','altairchart','scatter','linechart'])
        #select what you wanna know
        #columns grid
        #checked be in here
        column_chart = []
        #creat in number of columns->checkbox for it
        for i in col_list:
            che = st.checkbox(i,key = f"unique_1{i}")
            if che == True:
                column_chart.append(i)
        #show in plot
        for i in column_chart:
            if char == 'areachart':
                    st.area_chart(df, x=select_box_5, y=i)
            elif char == 'barchart':
                st.bar_chart(df, x=select_box_5, y=i)
            elif char == 'bokeh':
                p = figure(
                        title='simple line example',
                        x_axis_label=select_box_5,
                        y_axis_label=i)
                p.line(df[select_box_5], df[i], legend_label='Trend', line_width=2)
                st.bokeh_chart(p, use_container_width=True)  
            elif char == 'altairchart':
                c = (
                        alt.Chart(df)
                        .mark_circle()
                        .encode(x=select_box_5, y=i)
                        )

                st.altair_chart(c, use_container_width=True)
            elif char == 'scatter':
                st.scatter_chart(
                            df,
                            x=select_box_5,
                            y=i
                            )
            elif char == 'linechart':
                st.line_chart(df, x=select_box_5, y=i)
                
            elif char == 'boxplot1':
                c = alt.Chart(df).mark_boxplot(extent='min-max').encode(
                        x=f'{select_box_5}:O',
                        y=f'{i}:Q'
                    )
                st.altair_chart(c, theme="streamlit", use_container_width=True)
               
            elif char == 'boxplot2':
                fig = px.box(df, x=select_box_5, y=i)
                st.plotly_chart(fig, theme=None, use_container_width=True)
#=======================================
#for xlxs
#clean file

if vorodi != None:
    if '.xlsx' in vorodi.name:
        #read file
        df = pd.read_excel(vorodi)
        #columns for vector
        col_list = list(df.columns)
        #sort values
        check_sort = st.checkbox('Sort Values')
        if check_sort == True:
            select_box_sort = st.selectbox('what do you want for x',col_list,key='select_box_clean')
            df = df.sort_values(by=[select_box_sort], ignore_index=True,ascending=True)
            show_data = st.button('Show Data')
            if show_data == True:
                st.write(df)
        #select box
        '---------------'
        select_box = st.selectbox('what do you want for x',col_list)
        select_box_2 = st.selectbox('what do you want for y',col_list)

        #line chart for selectbox
        st.line_chart(df,x=select_box,y=select_box_2)
        '---------------------'
        #select chart and column you want
        charts = st.selectbox('what kind of chart you want?',['boxplot','areachart','barchart','bokeh','altairchart','scatter','linechart'])
        select_box_3 = st.selectbox('what do you need for x',col_list)
        select_col = st.selectbox('what you need for y',col_list)
        #all kind of charts
        if charts == 'areachart':
            st.area_chart(df, x=select_box_3, y=select_col)
        elif charts == 'barchart':
            st.bar_chart(df, x=select_box_3, y=select_col)
        elif charts == 'bokeh':
            p = figure(
                    title='simple line example',
                    x_axis_label=select_box_3,
                    y_axis_label=select_col)
            p.line(df[select_box_3], df[select_col], legend_label='Trend', line_width=2)
            st.bokeh_chart(p, use_container_width=True)  
        elif charts == 'altairchart':
            c = (
                alt.Chart(df)
                .mark_circle()
                .encode(x=select_box_3, y=select_col)
                )

            st.altair_chart(c, use_container_width=True)
        elif charts == 'scatter':
            st.scatter_chart(
                    df,
                    x=select_box_3,
                    y=select_col
                )
        elif charts == 'linechart':
            st.line_chart(df, x=select_box_3, y=select_col)
        elif charts == 'boxplot':
            fig = px.box(df, x=select_box_3, y=select_col)
            st.plotly_chart(fig, theme=None, use_container_width=True)

            '---------------------'
        '### everything you want just select it'
        #select what you wanna know
        #columns grid
        #checked be in here
        col_chart = []
        #creat in number of columns->checkbox for it
        select_box_4 = st.selectbox('select your x',col_list)
        col_1,col_2 = st.columns(2)
        for i in col_list:
            check = col_1.checkbox(i)
            if check == True:
                col_chart.append(i)
        #show in plot
        for i in col_chart:
            col_2.line_chart(df,x=select_box_4,y=i,height=500,width=700)
            '----------------------'
    
            '### select what chart and what column or columns you want to see'
            #select chart
        select_box_5 = st.selectbox('x',col_list)
        char = st.selectbox('chart',['boxplot1','boxplot2','areachart','barchart','bokeh','altairchart','scatter','linechart'])
            #select what you wanna know
            #columns grid
            #checked be in here
        column_chart = []
            #creat in number of columns->checkbox for it
        for i in col_list:
            che = st.checkbox(i,key = f"unique_1{i}")
            if che == True:
                column_chart.append(i)
            #show in plot
        for i in column_chart:
            if char == 'areachart':
                st.area_chart(df, x=select_box_5, y=i)
            elif char == 'barchart':
                st.bar_chart(df, x=select_box_5, y=i)
            elif char == 'bokeh':
                p = figure(
                        title='simple line example',
                        x_axis_label=select_box_5,
                        y_axis_label=i)
                p.line(df[select_box_5], df[i], legend_label='Trend', line_width=2)
                st.bokeh_chart(p, use_container_width=True)  
            elif char == 'altairchart':
                c = (
                        alt.Chart(df)
                        .mark_circle()
                        .encode(x=select_box_5, y=i)
                        )

                st.altair_chart(c, use_container_width=True)
            elif char == 'scatter':
                st.scatter_chart(
                            df,
                            x=select_box_5,
                            y=i
                            )
            elif char == 'linechart':
                st.line_chart(df, x=select_box_5, y=i)
            
            elif char == 'boxplot1':
                c = alt.Chart(df).mark_boxplot(extent='min-max').encode(
                        x=f'{select_box_5}:O',
                        y=f'{i}:Q'
                    )
                st.altair_chart(c, theme="streamlit", use_container_width=True)
               
            elif char == 'boxplot2':
                fig = px.box(df, x=select_box_5, y=i)
                st.plotly_chart(fig, theme=None, use_container_width=True)
