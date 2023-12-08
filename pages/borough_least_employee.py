import time
import numpy as np
import pandas as pd
import streamlit as st
from streamlit.hello.utils import show_code

# Placeholder function for data loading
def load_data(file_path):
    # Replace this with your actual data loading logic when data is available
    return pd.DataFrame()

# Function to visualize the data for each scenario
def plotting_demo(data, title):
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    st.markdown(f"# {title}")
    st.write(f"This graph shows distribution for {title}")
    st.button("Re-run")

    # Page 6: Borough with the Least Employees
    st.set_page_config(page_title="Borough with Least Employees", page_icon="🏙️")
    st.markdown("# Borough with Least Employees")
    st.sidebar.header("Borough with Least Employees")
    plotting_demo(load_data("path/to/your/borough_least_employees_data.csv"), "Borough with the Least Employees")


