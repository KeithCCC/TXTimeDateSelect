import streamlit as st
import time
import datetime


col0, col1, col2 = st.columns(3)

today=datetime.datetime.now().date()

options = ['Option1', 'Option2', 'Option3']



with col0:
    d = st.date_input("date", today)
    st.write('today')

with col1:
    t1 = st.time_input('start time', datetime.time(8, 45))
    st.write('start time ', t1)

with col2:
    t2 = st.time_input('End  time', datetime.time(9, 30))
    st.write('End time ', t2)

selected_option = st.selectbox('Select an option:', options)

st.write('Selcted:', selected_option)