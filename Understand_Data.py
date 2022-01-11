import pandas as pd
import pandas_profiling as pp
import streamlit as st
import streamlit_pandas_profiling as spp
data=pd.DataFrame()
@st.cache
def fun(data):
    profile=pp.ProfileReport(data)
    st.write(data)
    spp.st_profile_report(profile)
st.write('Understand your Data for better decision making.')
def m():
    file=st.file_uploader('Choose the file')
    if file is not None:
        data=pd.read_csv(file)
        fun(data)
if __name__=='__main__':
    m()
