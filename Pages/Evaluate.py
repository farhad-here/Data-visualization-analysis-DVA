#libraries
import streamlit as st
import numpy as np
import pandas as pd

file = st.file_uploader('DataSet')

#eval()


if file:
    df = pd.read_csv(file)
    st.caption('# Your dataset')
    st.dataframe(df)
    st.caption('# your dataset column')
    st.dataframe(df.columns)
    '## * evaluate *'
    st.info('''
            for exemple\n
                column1 + column2\n
                newcol = col1 + col2\n
                newcol2 = col2 + newcol\n             
            ''')
    name = st.text_input('name for column')
    if name:
        chat = st.chat_input('')
        if chat:
            order = pd.DataFrame(df.eval(f'{chat}'),columns=[name])
            st.dataframe(order)
            df = pd.concat((df,order),axis=1)
            st.dataframe(df)