import streamlit as st
import pandas as pd
from great_expectations.data_context import DataContext
from great_expectations.data_context import FileDataContext
import great_expectations as gx
import tempfile
import subprocess
import os

# Streamlit UI
st.title("Great Expectations with Streamlit")

# File Upload
file = st.file_uploader("Upload a CSV file", type=["csv"])

if file is not None:
    uploaded_file = pd.read_csv(file)


    st.subheader("Uploaded Data Preview")
    # df = pd.read_csv(uploaded_file)

    st.write(uploaded_file.head())

    st.subheader("Running Great Expectations")

    context = FileDataContext.create(project_root_dir=uploaded_file)

    context = gx.get_context()
    expectations_suite_name = "origin"

    validator = context.sources.pandas_default.read_csv(f"{uploaded_file}")

    # Give your Datasource a name
    datasource_name = "Man"
    datasource = context.sources.add_pandas(datasource_name)

    # Give your first Asset a name
    asset_name = "Prat"
    path_to_data = f"{uploaded_file}"
    
    asset = datasource.add_csv_asset(asset_name, filepath_or_buffer=path_to_data)

    # Build batch request
    batch_request = asset.build_batch_request()

    data_asset = context.get_datasource(datasource_name).get_asset(asset_name)
    batch_request = data_asset.build_batch_request()

    context.list_expectation_suite_names()

    context.add_or_update_expectation_suite(expectations_suite_name)

    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=expectations_suite_name)

    validator.expect_column_values_to_not_be_null("Credit Score")
    validator.expect_column_values_to_not_be_null("Number of Units")
    validator.expect_column_values_to_be_in_set("Number of Units", [1,2,3,4])
    validator.expect_column_median_to_be_between("Original Combined Loan-to-Value (CLTV)", min="10",max="100")
    validator.expect_column_values_to_be_in_set("Loan Purpose", ["P", "C", "N"])
    validator.expect_column_values_to_be_in_set("Occupancy Status", ["P", "I","S"])
    validator.expect_column_values_to_be_in_set("First Time Homebuyer Flag", ["Y", "N"])
    validator.expect_column_median_to_be_between("First Payment Date", 202201, 202212)

    validator.save_expectation_suite()

    checkpoint = context.add_or_update_checkpoint(
    name = "Og_Checkpoint",
    validator=validator)
    
    checkpoint_result = checkpoint.run(run_name="Run")

    context.build_data_docs()


    # Run Great Expectations

    # Display results
    st.subheader("Expectation Results")

    # Build data docs
    st.subheader("Building Data Docs")
    context.build_data_docs()

    # Display a link to the data docs
    data_docs_url = "URL_TO_YOUR_DATA_DOCS"  # Replace with your actual data docs URL
    st.write(f"Data Docs available at: [{data_docs_url}]({data_docs_url})")
