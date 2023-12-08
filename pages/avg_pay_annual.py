import streamlit as st
import pandas as pd

def money_paid_chart():
    st.sidebar.info("This page shows dynamic charts representing Total Money Paid and Inflation over Fiscal Years.")
    st.sidebar.warning("Note: The data is for demonstration purposes only.")

    # Data Table for Total Money Paid
    data_salary = {
        'Fiscal Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Total Money Paid (in Billions)': [22.86, 24.33, 25.52, 27.15, 27.55, 29.52, 30.42, 29.83, 31.74, 31.11]
    }

    df_salary = pd.DataFrame(data_salary)

    # Data Table for Inflation
    data_inflation = {
        'Fiscal Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Inflation Rate (%)': [1.6, -0.1, 1.4, 2.5, 2.1, 1.6, 2.5, 4.7, 8.0, 3.2]
    }

    df_inflation = pd.DataFrame(data_inflation)

    # Line Chart for Inflation
    st.line_chart(df_inflation.set_index('Fiscal Year'))

    # Bar Chart for Total Money Paid
    st.bar_chart(df_salary.set_index('Fiscal Year'))

def main():
    st.set_page_config(page_title="Data Visualization Pages", page_icon="📊")

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Select a page", ["Total Money Paid Chart"])

    if selected_page == "Total Money Paid Chart":
        st.markdown("# Total Money Paid Chart with Inflation")
        money_paid_chart()

if __name__ == "__main__":
    main()
