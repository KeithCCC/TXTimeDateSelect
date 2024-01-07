import pandas as pd
import streamlit as st
from datetime import datetime

data_df = pd.DataFrame(
    {
        "Start time": [
            datetime(2024, 2, 5, 12, 30),
            datetime(2023, 11, 10, 18, 0),
            datetime(2024, 3, 11, 20, 10),
            datetime(2023, 9, 12, 3, 0),
        ],
        "End time": [
            datetime(2024, 2, 5, 14, 30),
            datetime(2023, 11, 10, 19, 0),
            datetime(2024, 3, 11, 21, 10),
            datetime(2023, 9, 12, 4, 0),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "Start time": st.column_config.DatetimeColumn(
            "Start time",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="YYYY/MM/DD , h:mm a",
            step=60,
        ),
        "End time": st.column_config.DatetimeColumn(
            "End time",
            min_value=datetime(2023, 6, 1),
            max_value=datetime(2025, 1, 1),
            format="YYYY/MM/DD , h:mm a",
            step=60,
        ),
        "is_widget": "is_Widget ?",
    },
    hide_index=True,
)

# st.write(data_df)