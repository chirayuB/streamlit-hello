import time
import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code

# Placeholder function for data loading
def load_data(file_path):
    # Replace this with your actual data loading logic when data is available
    # For now, we'll return the provided data as a DataFrame
    data = {
        'Fiscal Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Number of People Left': [43638, 96958, 64033, 55830, 46992, 83606, 94357, 89281, 110725, 70743]
    }
    return pd.DataFrame(data)

# Function to visualize the data for the "Year with Most Jobs Lost" scenario
def plotting_demo(data, title):
    if data.empty:
        st.warning(f"No data available for {title}")
        return

    max_jobs_lost_year = data.loc[data['Number of People Left'].idxmax(), 'Fiscal Year']
    st.write(f"The fiscal year with the most jobs lost was {max_jobs_lost_year}.")

    st.bar_chart(data.set_index('Fiscal Year'))

    st.markdown(f"# {title}")
    st.write(f"This bar chart shows the number of people left each fiscal year.")
    st.button("Re-run")

# Page: Year with Most Jobs Lost
st.set_page_config(page_title="Year with Most Jobs Lost", page_icon="📉")
st.markdown("# Year with Most Jobs Lost")
st.sidebar.header("Year with Most Jobs Lost")
plotting_demo(load_data("path/to/your/year_most_jobs_lost_data.csv"), "Year with Most Jobs Lost")
