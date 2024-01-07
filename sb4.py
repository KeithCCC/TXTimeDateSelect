import streamlit as st

import time
import datetime
import pandas as pd

@st.cache_data
def init():
    # today=datetime.datetime.now().date()
    today = datetime.datetime.now()
    time1= datetime.time(0, 0)
    data = [[today , time1, time1]]
    df = pd.DataFrame(data, columns=["date", "start", "end"])
    print (today)
    return df, time1

count=0
df, time1 = init()
col0, col1, col2 = st.columns(3)
today = datetime.datetime.now()


with col0:
    d = st.date_input("date", today)
    # st.write('today')

with col1:
    t1 = st.time_input('start time', value=time1)
    # st.write('start time ', t1)

with col2:
    t2 = st.time_input('End  time', value=time1)
    # st.write('End time ', t2)


# st.button("remove apointment")
if st.button("Add apointment"):
    new_record = pd.DataFrame([{'date':pd.to_datetime(d),'start': t1, 'end':t2}])
    df = pd.concat([df, new_record])

try:
    st.write(df)
except Exception as e:
    print("Error")