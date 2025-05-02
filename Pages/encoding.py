import streamlit as st
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

"""
# lets Encode
"""
#Upload file
my_file = st.sidebar.file_uploader('Data')
#way of handle missing value select box
st.divider()
choice = st.selectbox('How you wanna encode it?',('OneHotEncoding','getDummies'))
#magic in here
st.divider()

if my_file != None:
    # GETDUMMIES
    df = pd.read_csv(my_file)
    if choice == 'getDummies':
        for i in df.columns:
            if df[i].dtype == object:
                x = pd.get_dummies(df[i],prefix=i,prefix_sep='_',dtype=float)
                df = pd.concat([df,x],axis=1)
                df.drop(columns=[i],inplace=True)
        
        b_data = st.button('Show Data',key='button get dummies')
        if b_data:
            st.dataframe(df)
        b_download_data = st.download_button(label='Download-DataSet',data=df.to_csv(index=False).encode('utf-8'),file_name=f'enc_{my_file.name}',mime="text/csv")
    #ONEHOTENOCDING
    elif choice == 'OneHotEncoding':
        ohe = OneHotEncoder(handle_unknown='ignore',sparse_output=False).set_output(transform='pandas')
        for i in df.columns:
            if df[i].dtype == object:
                ohe_transform = ohe.fit_transform(df[[i]])
                df = pd.concat([df,ohe_transform],axis=1).drop(columns=[i])
        b_data = st.button('Show Data',key='button OneHotEncoder')
        if b_data:
            st.dataframe(df)
        b_download_data = st.download_button(label='Download-DataSet',data=df.to_csv(index=False).encode('utf-8'),file_name=f'OHE_{my_file.name}',mime="text/csv")