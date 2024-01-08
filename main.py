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

# "st.session_state object:", st.session_state

st.title('Open appointment slot to string')

today = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)

# locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')


if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame(columns=["start", "end"])
    new_record = pd.DataFrame([{'start': today, 'end': today}])
    st.session_state.df = pd.concat([st.session_state.df, new_record])
    
df = init()

# Add button to add new record to the dataframe
if st.button("Add appointment"):
    new_record = pd.DataFrame([{'start': today, 'end': today}])
    st.session_state.df = pd.concat([st.session_state.df, new_record])
thirty_minutes = datetime.timedelta(minutes=30)
edited_df = st.data_editor(
    st.session_state.df,
        column_config={
        "start": st.column_config.DatetimeColumn(
            "start",
            format="YYYY年MM月DD日 hh:mm",
            step=thirty_minutes,
        ),
        "end": st.column_config.DatetimeColumn(
            "end",
            format="YYYY年MM月DD日 hh:mm",
            step=thirty_minutes,
        ),
    },
    # hide_index=True,
    num_rows="dynamic",
    width=800
    )

text_data="List of schedule\r\n"
# days = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
days = ['月', '火', '水', '木', '金', '土', '日']

if st.button("Convert"):
    st.session_state.df = edited_df
    for index, row in st.session_state.df.iterrows():
        start_data = row['start']
        DoWstart = days[start_data.weekday()]
        str_start = str(start_data.year) + '年' + str(start_data.month) + '月' + str(start_data.day) + '日 (' + DoWstart + ') ' +str(start_data.hour) + ':' + str(start_data.minute) 
        
        end_data = row['end']
        DoWend= days[end_data.weekday()]
        str_end = str(end_data.year) + '年' + str(end_data.month) + '月' + str(end_data.day) + '日 (' + DoWend + ') ' +str(end_data.hour) + ':' + str(end_data.minute) 

        text_data += f"{str_start} - {str_end} \r\n"
        print (str_start,end_data )
    # text_data = st.session_state.df.to_string(index=False)
    st.text(text_data)

# st.table(st.session_state.df)
# st.table(edited_df)