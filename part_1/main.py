import streamlit as st
import requests
from io import BytesIO
from PyPDF2 import PdfReader
import nougat
import base64

# Function to extract text from a PDF using PyPDF2
def extract_text_pypdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to summarize text using Nougat
def summarize_text_nougat(text):
    summarizer = nougat.Nougat()
    summary = summarizer.summarize(text)
    return summary

st.title("PDF Summary App")

# User input for the PDF link
pdf_link = st.text_input("Enter the link to the PDF file:")

# User selection for the PDF processing library
pdf_library = st.radio("Select PDF processing library:", ("PyPDF2", "Nougat"))

if st.button("Generate Summary"):
    if pdf_link:
        try:
            # Download the PDF file
            response = requests.get(pdf_link)
            pdf_content = response.content

            if pdf_library == "PyPDF2":
                # Extract text using PyPDF2
                text = extract_text_pypdf(BytesIO(pdf_content))
                st.subheader("Summary:")
                st.write(text)  # Display the extracted text
                
                # Calculate and display the length of the PDF and summary
                st.subheader("Length of PDF:")
                st.write(len(pdf_content))
                st.subheader("Length of Summary:")
                st.write(len(text))
            else:
                # Extract text using Nougat
                pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
                text = pdf_base64
                summary = summarize_text_nougat(text)
                st.subheader("Summary:")
                st.write(summary)

                # Calculate and display the length of the PDF and summary
                st.subheader("Length of the uploaded PDF:")
                st.write(len(pdf_content))
                st.subheader("Length of the generated Summary:")
                st.write(len(summary))

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please enter a valid PDF link.")
