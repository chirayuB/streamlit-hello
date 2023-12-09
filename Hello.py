import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="NYC Payroll Analysis",
        page_icon="👋",
    )

    st.write("# New York City Municipal Employee Pay Data Analysis ")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
       This project proposal aims to conduct an in-depth analysis of the New York City Municipal Employee Pay Data to provide valuable insights into how the city's budget is allocated towards employee salaries and overtime pay. The data is collected and maintained within the City's Personnel Management System (“PMS”) by various user agencies, and it has become increasingly essential due to public interest in fiscal transparency and accountability.

    """
    )


if __name__ == "__main__":
    run()
