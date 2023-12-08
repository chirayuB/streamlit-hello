import streamlit as st
import pandas as pd

def start_month_chart():
    st.sidebar.info("This page shows a dynamic chart representing the number of employees who started working by month.")
    st.sidebar.warning("Note: The data is for demonstration purposes only.")

    # Data Table - Start Month
    data_start_month = {
        'Start Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Count': [806338, 359621, 326249, 295443, 243674, 291376, 473886, 407760, 1520957, 389203, 262177, 285966]
    }

    df_start_month = pd.DataFrame(data_start_month)

    # Convert 'Start Month' to categorical with custom order
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_start_month['Start Month'] = pd.Categorical(df_start_month['Start Month'], categories=months_order, ordered=True)

    # Sort DataFrame by the custom order of months
    df_start_month = df_start_month.sort_values(by='Start Month')

    # Chart - Bar Chart for Number of Employees by Start Month
    st.bar_chart(df_start_month.set_index('Start Month'))

def main():
    st.set_page_config(page_title="Data Visualization Pages", page_icon="📊")

    st.markdown("# Start Month Chart")
    start_month_chart()

if __name__ == "__main__":
    main()
