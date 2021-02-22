import streamlit as st
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

#Buat Judul
st.title('''EDA Apps

Oleh : Nezar Abdilah Prakasa

Let's Check your data profiling!
''')

#Upload CSV
with st.sidebar.header('Upload data CSV'):
    uploaded_file=st.sidebar.file_uploader('Upload datamu!', type=['csv'])

#Pandas Profiling
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv= pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input Data Frame**')
    st.write(df)
    st.write('---')
    st.header('***Report***')
    st_profile_report(pr)
else:
    st.info ('Menunggu Data di Upload')
    if st.button('Tekan untuk Menggunakan Data Contoh'):
        #Contoh Data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100,5),
                columns=['a','b','c','d','e']
            )
            return a
        df=load_data()
        pr=ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('----')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)