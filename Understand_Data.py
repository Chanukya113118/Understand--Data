import pandas as pd
import pandas_profiling as pp
import streamlit as st
import streamlit_pandas_profiling as spp
data=pd.DataFrame()
@st.cache(allow_output_mutation=True,max_entries=100,ttl=5000)
def fun(data):
    profile=pp.ProfileReport(data)
    st.write(data)
    spp.st_profile_report(profile)
st.write('Understand your Data for better decision making.')
file=st.file_uploader('Choose the file')
if file is not None:
    data=pd.read_csv(file)
    fun(data)
        
