import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import time
import tempfile
import base64
import os

# Set Streamlit app title
st.title('Pandas Profiling App')

def run_colab_notebook_origination():
    # Replace 'YOUR_COLAB_NOTEBOOK_URL' with the actual Colab notebook URL
    colab_notebook_url = 'https://colab.research.google.com/drive/1RfLX5bc-ilPhwFGjqGH5Mf584CE1SG_i#scrollTo=n7DyaLoXNUTY'

    link_text = "Click here to view great expectations for origination data"

    # Create a hyperlink using Markdown
    st.markdown(f"[{link_text}]({colab_notebook_url})")

def run_colab_notebook_monthly():
    # Replace 'YOUR_COLAB_NOTEBOOK_URL' with the actual Colab notebook URL
    colab_notebook_url = 'https://colab.research.google.com/drive/1p4PT3s-5Lpsf6eFsTkKodBfJe6UPGsIe'

    link_text = "Click here to view great expectations for monthly performance data"

    # Create a hyperlink using Markdown
    st.markdown(f"[{link_text}]({colab_notebook_url})")



# Upload a file
uploaded_file = st.file_uploader("Upload a CSV or XLS file", type=["csv", "xls", "xlsx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1].lower()
    
    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_extension in ["xls", "xlsx"]:
        df = pd.read_excel(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a CSV or Excel file.")
        st.stop()

    # Display the DataFrame
    st.write("Uploaded DataFrame:")
    st.write(df)

    # Dropdown for Pandas Profiling options
    profiling_option = st.selectbox("Choose an option:", ["Origination Data", "Monthly Performance Data"])

    if st.button("Generate Pandas Profiling"):  # Add a button to start report generation
        if profiling_option == "Origination Data":
            run_colab_notebook_origination()
            # Create an empty text element for progress updates
            progress_text = st.empty()

            # Perform Pandas Profiling for Origination Data
            profile = ProfileReport(df, title="Origination Data Profiling Report", explorative=True)

            # Simulate progress and update the progress text
            for percent_complete in range(101):
                progress_text.text(f"Pandas Profiling Report is {percent_complete}% complete.")
                if percent_complete == 100:
                    time.sleep(2)  # Wait for 2 seconds at 100% progress
                time.sleep(0.1)  # Simulate processing time

            # Display a loading message while generating the report
            progress_message = st.info("Generating the report. Please wait...")

            # Remove the "Pandas Profiling Report is 100% complete." message
            progress_text.empty()

            # Save the report as an HTML file

            newpath = "temp"
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            # temp_dir = tempfile.mkdtemp()
            report_path = f"{newpath}/origination_data_profile_report.html"
            profile.to_file(report_path)

            # Remove the loading message and display the report
            progress_message.empty()
            st.write(f"### Pandas Profiling Report")
            st.markdown(f'<iframe src="data:text/html;base64,{base64.b64encode(open(report_path, "rb").read()).decode()}" height="1000" width="100%"></iframe>', unsafe_allow_html=True)
            st.write("Pandas Profiling Report is complete.")
        elif profiling_option == "Monthly Performance Data":
            run_colab_notebook_monthly()
            # Create an empty text element for progress updates
            progress_text = st.empty()

            # Perform Pandas Profiling for Monthly Performance Data
            profile = ProfileReport(df, title="Monthly Performance Data Profiling Report", explorative=True)

            # Simulate progress and update the progress text
            for percent_complete in range(101):
                progress_text.text(f"Pandas Profiling Report is {percent_complete}% complete.")
                if percent_complete == 100:
                    time.sleep(2)  # Wait for 2 seconds at 100% progress
                time.sleep(0.1)  # Simulate processing time

            # Display a loading message while generating the report
            progress_message = st.info("Generating the report. Please wait...")

            # Remove the "Pandas Profiling Report is 100% complete." message
            progress_text.empty()

            # Save the report as an HTML file
            temp_dir = tempfile.mkdtemp()
            report_path = f"{temp_dir}/monthly_performance_data_profile_report.html"
            profile.to_file(report_path)

            # Remove the loading message and display the report
            progress_message.empty()
            st.write(f"### Pandas Profiling Report")
            st.markdown(f'<iframe src="data:text/html;base64,{base64.b64encode(open(report_path, "rb").read()).decode()}" height="1000" width="100%"></iframe>', unsafe_allow_html=True)
            st.write("Pandas Profiling Report is complete.")
        else:
            st.warning("Select a valid profiling option from the dropdown.")

# Add a footer
st.markdown("---")
st.write("Created by Huskies 🐾")
