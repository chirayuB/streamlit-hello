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
        'Work Location Borough': ['BRONX'] * 9 + ['BROOKLYN'] * 9 + ['MANHATTAN'] * 9 + ['QUEENS'] * 9,
        'Fiscal Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023] * 4,
        'avg_salary': [
            44626.27237027824, 46477.41344662518, 44402.213804788356, 49584.07435367719, 50989.31965118259,
            52735.95984245874, 55290.460385715865, 56176.966789944636, 58352.566308159156,
            48105.01605357891, 50253.5810881394, 49710.4538667813, 52776.89150342302, 53787.940628325996,
            55156.42707844183, 59288.81568700936, 61179.80880595006, 62048.86133170584,
            32799.149828488866, 37826.68599229443, 38474.94777980713, 40783.48690581132, 39569.77024472954,
            42090.37713661531, 43044.49212383632, 42768.40343145001, 46735.63884644754,
            47721.84717897886, 50649.58732148246, 48482.80001271844, 52137.553875261605, 52340.30731768547,
            52391.942484636405, 58846.691719808914, 60072.21605640129, 61467.49201467067
        ]
    }
    return pd.DataFrame(data)

# Function to visualize the data for the "Average Salary by Borough" scenario
def plotting_demo(data, title):
    if data.empty:
        st.warning(f"No data available for {title}")
        return

    st.line_chart(data.set_index(['Fiscal Year', 'Work Location Borough']))

    st.markdown(f"# {title}")
    st.write(f"This line chart shows the average salary for each borough over the years.")
    st.button("Re-run")

# Page: Average Salary by Borough
st.set_page_config(page_title="Average Salary by Borough", page_icon="💵")
st.markdown("# Average Salary by Borough")
st.sidebar.header("Average Salary by Borough")
plotting_demo(load_data("path/to/your/average_salary_by_borough_data.csv"), "Average Salary by Borough")
