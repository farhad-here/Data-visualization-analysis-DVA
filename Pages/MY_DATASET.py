#libraries
import streamlit as st
import pandas as pd
import io

'''
# In this page you can play with your DataSet
'''
#upload data set
st.divider()
'''## * Upload file Section *'''
file = st.file_uploader('DataSet')
st.divider()
if file != None:
    #read dataset
    df = pd.read_csv(file)
    #show my DataSet
    '## * DataSet Section *'
    st.dataframe(df)
    st.divider()
    #See and know about data set or the part you want
    '## * know about your dataset or the specefic part you want to know Section *'
    #head
    st.caption('# Head')
    num = st.number_input('The number of first samples you want to see',step=1,key='number inp head')
    if num:
        st.dataframe(df.head(num))
    #tail
    st.caption('# Tail')
    num_2 = st.number_input('The number of first samples you want to see',step=1,key='number inp tail')
    if num_2:
        st.dataframe(df.tail(num_2))
    #Ndim,Size,Shape,describe
    col_ndim,col_size,col_shape = st.columns(3)
    col_ndim.caption('# Ndim')
    but_ndim = col_ndim.button('Show me the number of axes/array dimensions',key='button ndim')
    if but_ndim:
        col_ndim.write(df.ndim)

    col_size.caption('# size')
    but_size = col_size.button('give me my dataset size',key='button size')
    if but_size:
        col_size.write(df.size)
        
    col_shape.caption('# shape')
    but_shape = col_shape.button('show my dataset shape',key='button shape')
    if but_shape:
        col_shape.write(df.shape)
    # #INFO
    # st.caption('# info')
    # but_info = st.button('Show me the information',key='button info')
    # if but_info:
    #     buffer_info = io.StringIO() 
    #     df.info(buf=buffer_info)
    #     job_info = buffer_info.getvalue()
    #     with open("df_info.csv", "w", ) as f:
    #         f.write(list(job_info)) 
    #     st.write(job_info)
    st.divider()
    #columns and index
    '## * column and index Section*'
    col_show_b = st.button('Show',key='col_show_butt_1')
    if col_show_b:
        col_col_1,col_index_1 = st.columns(2)
        col_col_1.caption('## columns')
        col_col_1.dataframe(df.columns,width=300)
        col_index_1.caption('## index/row')
        col_index_1.dataframe(df.index,width=300)
    # ABS()
    '## * Absolute value Section*'
    abs_b = st.button('DO',key=('abs1'))
    if abs_b:
        st.dataframe(df.abs(),width=600)

    st.divider()
    #remove
    '## * remove section *'
    st.caption('### **like this col1,col2,...**')
    rem_col_name = st.text_input('Name column/feature',key='remove col name1')
    rem_col_b = st.button('Do',key='remove col button1')
    st.divider()
    if rem_col_name and rem_col_b:
        col_for_remove_names = rem_col_name.split(',')
        df.drop(columns=col_for_remove_names,inplace=True)
        st.dataframe(df)
    
    #replace
    '## * Change/replace name Section *'
    st.caption('# replace')
    sample_nreplace = st.text_input('What do you want to replace?',key='replace1')
    sample_nreplace2 = st.text_input('replace it into what?',key='replace2')
    sample_nreplace3 = st.text_input('what column?',key='replace3')
    sample_nreplace_b = st.button('Replace',key='replace button1')
    if sample_nreplace2 == None:
        sample_nreplace2 = ''
    if sample_nreplace and  sample_nreplace3 and sample_nreplace_b:
        name_replace_func = lambda l:l.replace(sample_nreplace,sample_nreplace2)
        df[sample_nreplace3] = df[sample_nreplace3].apply(name_replace_func)
        st.dataframe(df[sample_nreplace3],width=500)
        st.dataframe(df,width=700)
    st.caption('# rename a column name')
    #rename
    ren_col_inp = st.text_input('column name',key='ren col1')
    ren_col_inp2 = st.text_input('rename into what?',key='ren col2')
    ren_col_button = st.button('Do',key='ren button1')
    if ren_col_inp and ren_col_inp2 and ren_col_button:
        df.rename({ren_col_inp:ren_col_inp2},axis=1,inplace=True)
        st.dataframe(df)
    st.divider()
    #total samples in feature value_counts()
    '## * total number of samples in feature *'
    value_count_1 = st.text_input('Feature',key='val_count_1')
    value_count_b_1 = st.button('Show',key='show button value_counts1')
    if value_count_1 and value_count_b_1:
        st.dataframe(df[value_count_1].value_counts(),width=600)
        
    st.divider()
    #MAX OR MIN
    '## * Maximum and Minimum Section *'
    col_minmax_1,col_minmax_2 = st.columns(2)
    ch_mx_1 = col_minmax_1.checkbox('All Features Mean',key='ch_minmax')
    ch_mx_2 = col_minmax_2.checkbox('My specific feature Mean',key='ch_meanmax2')
    if ch_mx_1:
        ch_minmax_3,ch_minmax_4 = st.columns(2)
        ch_minmax_3.caption('# MIN')
        ch_minmax_3.dataframe(df.min(),width=500)
        ch_minmax_4.caption('# MAX')
        ch_minmax_4.dataframe(df.max(),width=500)
    elif ch_mx_2:
        fea = st.text_input('Feature')
        if fea:
            ch_minmax_3,ch_minmax_4 = st.columns(2)
            ch_minmax_3.caption('# MIN')
            ch_minmax_3.dataframe(df[[fea]].min(),width=500)
            ch_minmax_4.caption('# MAX')
            ch_minmax_4.dataframe(df[[fea]].max(),width=500)
    st.divider()
    #MEAN For MY DATASET
    '## * MEAN Section *'
    col_mean_1,col_mean_2 = st.columns(2)
    ch_mean_1 = col_mean_1.checkbox('All Features Mean',key='ch_mean1')
    ch_mean_2 = col_mean_2.checkbox('My specific feature Mean',key='ch_mean2')
    if ch_mean_1:
        st.dataframe(df.mean(),width=600)
    elif ch_mean_2:
        fea_mean = st.text_input('Name of feature you want')
        if fea_mean:
            st.dataframe(df[[fea_mean]].mean(),width=600)
    st.divider()
    #standard Deviation
    "## *Standard Deviation Section *"
    col_std_1,col_std_2 = st.columns(2)
    ch_std_1 = col_std_1.checkbox('All Features std',key='ch_std')
    ch_std_2 = col_std_2.checkbox('My specific feature std',key='ch_std2')
    if ch_std_1:
        st.dataframe(df.std(),width=600)
    elif ch_std_2:
        fea_std = st.text_input('Name of feature you want')
        if fea_std:
            st.dataframe(df[[fea_std]].std(),width=600)
    st.divider()
    #describe
    '## * Describe Section *'
    des_b = st.button('Describe')
    if des_b:
        st.dataframe(df.describe(),width=700)
    st.divider()
    #MISSING VALUE
    '## * ABOUT MISSING VALUE Section *'
    '* ### find missing value'
    t_f_missing = st.button('SHOW ME MISSING')
    if t_f_missing:
        st.dataframe(df.isna())
    '* ### find missing value in specefic feature'
    fea_miss = st.text_input('Feature',key='fea_miss')
    missingVal_1 = st.button('SHOW ME MISSING',key='Miss1')
    if fea_miss and missingVal_1:
        st.dataframe(df[[fea_miss]].isna())
    '* ### number of missing values'
    missingVal_2 = st.button('SHOW ME number of MISSING values of all features',key='Miss2')
    if missingVal_2:
        st.dataframe(df.isna().sum(),width=700)
    fea_num_miss = st.text_input('Feature')
    missingVal_3 = st.button('Show me number of missing value in that specific feature that i want')
    if fea_num_miss:
        if missingVal_3:
            st.dataframe(df[[fea_num_miss]].isna().sum(),width=400)
    '* ### number of missing values in a row and column'
    button_number_missing_row_col = st.button('Show')
    if button_number_missing_row_col:
        st.caption('# row')
        st.dataframe(df.isna().sum(axis=1),width=700)
        st.caption('# column')
        st.dataframe(df.isna().sum(axis=0),width=700)
    b_total_miss = st.button('total number of rows with missing values')
    if b_total_miss:
        st.write(f'- [x] total number of rows with missing values: {(df.isna().sum(axis=1)).sum()} rows')
    st.divider()
    #FIND UNIQUE
    '## * Find Unique values in feature *'
    feature_uniq = st.text_input('Feature',key='FeatureUnique1')
    feature_uniq_button = st.button('SHow',key='featur unique button 1')
    if feature_uniq and feature_uniq_button:
        st.caption('## total number of unique item in that feature')
        st.write(f'### We have *{len(df[feature_uniq].unique())}* unique smaples in that feature')
        st.caption('## Unique items we have in that feature')
        st.dataframe(df[feature_uniq].unique(),width=700)

    st.divider()
    #correlatrion
    '## * correlation Section *'
    st.caption('# How well the relationship between columns')
    st.caption('### col1,col2,...')
    corr_inp = st.text_input('column name',key='corr inp1')
    corr_button = st.button('show',key='corr button1')
    if corr_button and corr_inp:
        list_col_corr = corr_inp.split(',')            
        st.dataframe(df[list_col_corr].corr())
    st.caption('# for corr Dataset')    
    corr_button2 = st.button('show for all',key='corr button2')
    if corr_button2:
        st.dataframe(df.corr())

    st.divider()