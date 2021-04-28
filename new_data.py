import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

st.title('Status of Survey about covid')
#st.write("It shows ***PC level analysis*** in Tirupati PC")
st.sidebar.title("Selector")
#image = Image.open("PC.jpg")
#st.image(image,use_column_width=False)
st.markdown('<style>body{background-color: lightblue;}Survey</style>',unsafe_allow_html=True)
#container=st.beta_container()
st.markdown("## **Actual data of survey**")
@st.cache
def load_data():
    df = pd.read_csv("https://docs.google.com/spreadsheets/d/1gbyu86do0F74tNW3gnWCDt6UrmaCi_KCDDykv-Mz1Mc/export?format=csv&gid=1705347459")
    return df

df = load_data()
#st.write(df)

#data=df[df['Status of Call']=='Call Responded']
#st.write(data)



def get_table():
    datatable = df[['Phone number', 'Gender', 'Are you infected with Covid-19',
                    'How are you feeling now',
                    'Did you had any symptoms?',
                    'Please Mention Symptoms','Do you have Negative report?','Are you willing to donate Plasma','At what time will you be available to donate Plasma?',
                    'Age ']].sort_values(by=['Gender'],ascending =True)
    return datatable

datatable = get_table()
st.markdown("***Data which was used for plot***")
st.dataframe(datatable)
select_Gender = st.sidebar.selectbox('Select a Gender',datatable['Gender'].unique())
#st.write(select_gender)
#select_Group = st.sidebar.selectbox('Select a Blood Group',datatable['Blood Group?'].unique())
#select_Location = st.sidebar.selectbox('Select a location',datatable['Location of Respondent?'].unique())

selected_data = datatable[datatable['Gender']==select_Gender]
#st.write("gender",selected_data)
#selected_location = selected_data[selected_data['Location of Respondent?']==select_Location]
#st.write("location",selected_location)
#selected_group = selected_location[selected_location['Blood Group?']==select_Group]
st.write("Final Data",selected_data)


