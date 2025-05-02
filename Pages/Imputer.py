import streamlit as st
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np

"""
# lets handle Missing value
"""
#Upload file
my_file = st.sidebar.file_uploader('Data')
#way of handle missing value select box
choice = st.selectbox('How you wanna handle it?',('KNNIMPUTER','DropNa','FillNa','loc'))
#MAIN CODE
if my_file != None:
    df = pd.read_csv(my_file)
    #KNNIMPUTER
    if choice == 'KNNIMPUTER':
        st.caption('### DATASET before KNN')
        st.dataframe(df)
        df_arr = df.to_numpy()
        n_neigh_knn = st.text_input('for N_neighbor_KNN')
        w_knn = st.selectbox('select for weights KNNIMputer',['distance','uniform'],key='weights KNN')
        if n_neigh_knn:
            imput = KNNImputer(n_neighbors=int(n_neigh_knn),weights=w_knn)
            impute_array = imput.fit_transform(df_arr)
            df = pd.DataFrame(data=impute_array,columns=df.columns,index=df.index)
            st.caption('### DATASET after KNN')
            st.dataframe(df)
            make_data_int = st.checkbox('I DONT WANT FLOAT-_-')
            if make_data_int:
                st.caption('# input like this for example age or age,education,...')
                feature_name = st.text_input('name of the feature to be int :)')
                list_feature = feature_name.split(',')
                if feature_name:
                    for i in list_feature:
                        df[f"{i}"]= df[f"{i}"].astype(int)
                    st.dataframe(df)
    #DROPNA
    elif choice =='DropNa':
        st.caption('DataSet before dropna')
        st.dataframe(df)
        st.caption('## limit For How Much Valid Data is OK')
        thresh_hold =st.number_input('thresh',step=1)
        st.caption('## 0 (INDEX/ROW) & 1 (columns)')
        axis_hold = st.number_input('axis',min_value=0,max_value=1,step=1)
        if thresh_hold == 0:
            df = df.dropna(axis=axis_hold)
        else:
            df = df.dropna(axis=axis_hold,thresh=thresh_hold)
        st.caption('DataSet after dropna')
        b_showdata_afterDropna = st.button('Show Data') 
        if b_showdata_afterDropna:
            st.dataframe(df)
    #FILLNA
    elif choice == 'FillNa':
        #fill all missing value
        col_fill_na1,col_fill_na2 = st.columns(2)
        fna1 = col_fill_na1.checkbox('Fill all Nan')
        fna2 = col_fill_na2.checkbox('fill my specific feature')
        if fna1:
            inp_fill = st.number_input('fill with what?')
            if inp_fill:
                df.fillna(inp_fill,inplace=True)
                st.dataframe(df)
        elif fna2:
            inp_fill = st.number_input('fill with what?')
            inp_fill_fea = st.text_input('what feature?')
            if inp_fill and inp_fill_fea:
                df[inp_fill_fea].fillna(inp_fill,inplace=True)
                st.dataframe(df)
    #loc
    elif choice == 'loc':
        st.caption('## dataset before handling the missing value')
        st.dataframe(df)
        st.divider()
        st.caption('## the index i want(row name)')
        ind = st.text_input('INDEX')
        st.caption('## the feature i want(column name)')
        fea = st.text_input('FEATURE')
        st.caption('## what should be')
        be = st.number_input('what should be in the missing value?')
        if ind and fea and be:
            index_type =df.index.dtype
            if 'int' in f'{index_type}':
                df.loc[int(ind),fea]=be
            elif 'float' in f'{index_type}':
                df.loc[float(ind),fea]=be
            else:
                df.loc[ind,fea]=be
            st.divider()
            st.caption('## dataset after handdling missing value')
            st.dataframe(df)