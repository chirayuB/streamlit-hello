import streamlit as st
import pandas as pd
import altair as alt

def start_month_chart():
    st.sidebar.info("This page shows a dynamic chart representing the number of employees who started working by month.")
    st.sidebar.warning("Note: The data is for demonstration purposes only.")

    # Data Table - Start Month
    data_start_month = {
        'Start Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Count': [806338, 359621, 326249, 295443, 243674, 291376, 473886, 407760, 1520957, 389203, 262177, 285966]
    }

    df_start_month = pd.DataFrame(data_start_month)

    # Chart - Bar Chart for Number of Employees by Start Month
    chart = alt.Chart(df_start_month).mark_bar().encode(
        x=alt.X('Start Month:N', sort=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']),
        y='Count:Q'
    ).properties(
        width=600,
        height=400
    )

    st.altair_chart(chart)

def main():
    st.set_page_config(page_title="Data Visualization Pages", page_icon="📊")

    st.markdown("# Start Month Chart")
    start_month_chart()

if __name__ == "__main__":
    main()
