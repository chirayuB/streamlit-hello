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
        'Total Money Paid (in Billions)': [22.86, 24.33, 25.52, 27.15, 27.55, 29.52, 30.42, 29.83, 31.74, 31.11]
    }
    return pd.DataFrame(data)

# Function to visualize the data for the "Total Annual Salary" scenario
def plotting_demo(data, title):
    if data.empty:
        st.warning(f"No data available for {title}")
        return

    st.bar_chart(data.set_index('Fiscal Year'))

    st.markdown(f"# {title}")
    st.write(f"This bar chart shows the total money paid (in billions) each fiscal year.")
    st.button("Re-run")

# Page: Total Annual Salary
st.set_page_config(page_title="Total Annual Salary", page_icon="💰")
st.markdown("# Total Annual Salary")
st.sidebar.header("Total Annual Salary")
plotting_demo(load_data("path/to/your/total_annual_salary_data.csv"), "Total Annual Salary")
