import streamlit as st
import pandas as pd
import datetime
import datetime as dt
import locale

# Create an empty dataframe
@st.cache_data
def init():
    st.session_state.df = pd.DataFrame(columns=["start", "end"])
    return st.session_state.df

"st.session_state object:", st.session_state

today = datetime.datetime.now()
locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')

if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=["start", "end"])
    new_record = pd.DataFrame([{'start': today, 'end': today}])
    st.session_state.df = pd.concat([st.session_state.df, new_record])
    
df = init()

# Add button to add new record to the dataframe
if st.button("Add appointment"):
    new_record = pd.DataFrame([{'start': today, 'end': today}])
    st.session_state.df = pd.concat([st.session_state.df, new_record])

st.data_editor(
    st.session_state.df,
        column_config={
        "start": st.column_config.DatetimeColumn(
            "start",
            format="YYYY年MM月DD日 hh:mm",
            step=30,
        ),
        "end": st.column_config.DatetimeColumn(
            "end",
            format="YYYY年MM月DD日 hh:mm",
            step=0,
        ),
        
    },
    hide_index=True,
    num_rows="dynamic",
    width=800
    )

text_data="List of schedule\r\n"

if st.button("Convert"):
    for index, row in st.session_state.df.iterrows():
        text_data += f"{row['start']} - {row['end']}\r\n"
        print (row['start'],row['end'] )
    # text_data = st.session_state.df.to_string(index=False)
    st.write(text_data)


# Display the dataframe
# st.write(st.session_state.df)

# for the_values in st.session_state.values():
#     st.write(the_values)