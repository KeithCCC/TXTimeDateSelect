import pandas as pd
import streamlit as st
import datetime

# Create a pandas DataFrame with today's date and two time columns
now = datetime.datetime.now()
data = {'start': [now], 'end': [now]}
df = pd.DataFrame(data)

if st.button("Add"):
    new_row = {'start': now, 'end': now}
    df = df.append(new_row, ignore_index=True)
    
st.write(df)