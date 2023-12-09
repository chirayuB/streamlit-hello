import streamlit as st

# Function to visualize the data for the "Average Salary by Borough" scenario
def plotting_demo(data, title):
    if data.empty:
        st.warning(f"No data available for {title}")
        return

    # Replace the placeholder URL with the provided image URL
    chart_image_url = "https://i.postimg.cc/hvJBWj1V/Screenshot-2023-12-09-at-11-20-20-AM.png"

    st.image(chart_image_url, use_container_width=True)

    st.markdown(f"# {title}")
    st.write(f"This is a placeholder chart image for {title}.")
    st.button("Re-run")

# Page: Average Salary by Borough
st.set_page_config(page_title="Average Salary by Borough", page_icon="💵")
st.markdown("# Average Salary by Borough")
st.sidebar.header("Average Salary by Borough")
plotting_demo(load_data("path/to/your/average_salary_by_borough_data.csv"), "Average Salary by Borough")
