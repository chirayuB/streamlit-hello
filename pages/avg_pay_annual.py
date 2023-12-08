import streamlit as st
import pandas as pd

def money_paid_chart():
    st.sidebar.info("This page shows a dynamic chart representing Total Money Paid over Fiscal Years.")
    st.sidebar.warning("Note: The data is for demonstration purposes only.")

    # Data Table
    data = {
        'Fiscal Year': [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Total Money Paid (in Billions)': [22.86, 24.33, 25.52, 27.15, 27.55, 29.52, 30.42, 29.83, 31.74, 31.11]
    }

    df = pd.DataFrame(data)

    # Chart
    st.line_chart(df.set_index('Fiscal Year'))

def main():
    st.set_page_config(page_title="Data Visualization Pages", page_icon="📊")

    st.sidebar.title("Navigation")
    selected_page = st.sidebar.selectbox("Select a page", ["Total Money Paid Chart"])

    if selected_page == "Total Money Paid Chart":
        st.markdown("# Total Money Paid Chart")
        money_paid_chart()

if __name__ == "__main__":
    main()
