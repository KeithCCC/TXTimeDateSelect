import streamlit as st
import pandas as pd

# Create an empty dataframe
@st.cache_data
def init():
    st.session_state.df = pd.DataFrame(columns=["date", "start", "end"])
    return st.session_state.df

"st.session_state object:", st.session_state

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=["date", "start", "end"])
    
df = init()

# st.write(st.session_state.df)
# Define the UI elements
col0, col1, col2 = st.columns(3)
with col0:
    d = st.date_input("date", pd.to_datetime('today'), key="date_input")
with col1:
    t1 = st.time_input('start time', key="start_time_input")
with col2:
    t2 = st.time_input('End time', key="end_time_input")


# Add button to add new record to the dataframe
if st.button("Add appointment"):
    new_record = pd.DataFrame([{'date': d, 'start': t1, 'end': t2}])
    st.session_state.df = pd.concat([st.session_state.df, new_record])

# Display the dataframe
st.write(st.session_state.df)

for the_values in st.session_state.values():
    st.write(the_values)