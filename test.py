import streamlit as st
import pandas as pd

# データを読み込む
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

# データを表示する
if "df" not in st.session_state:
    st.session_state.df = df

edited_df = st.data_editor(st.session_state.df)

# 変更を保存する
if st.button("Save Changes"):
    st.write("Changes saved!")