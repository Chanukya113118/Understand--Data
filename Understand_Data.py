import pandas as pd
import pandas_profiling as pp
import streamlit as st
import streamlit_pandas_profiling as spp
data=pd.DataFrame()
def fun(data):
    profile=pp.ProfileReport(data)
    st.write(data)
    spp.st_profile_report(profile)
st.title('Understand Data')
def m():
    try:
        file=st.file_uploader('Choose the file')
        if file is not None:
           try:
                data=pd.read_csv(file)
                fun(data)
           except:
                try:
                    data=pd.read_csv(file)
                    fun(data)  
                except:
                    st.write('')
    except:
        st.write("Enter CSV or Excel files only please try again")
if __name__=='__main__':
    m()
