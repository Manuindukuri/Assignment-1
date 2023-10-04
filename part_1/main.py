import streamlit as st
import subprocess
import requests
from io import BytesIO
from PyPDF2 import PdfReader
import base64

# Function to extract text from a PDF using PyPDF2
def extract_text_pypdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def run_colab_notebook():
    # Replace 'YOUR_COLAB_NOTEBOOK_URL' with the actual Colab notebook URL
    colab_notebook_url = 'https://colab.research.google.com/drive/1m6HVtjNsZv_ru3n7ykfRDCmd73zhYAdA#scrollTo=JLXCdVCNULDm'

<<<<<<< Updated upstream
st.title("PDF Summary App")

# User input for the PDF link
pdf_link = st.text_input("Enter the link to the PDF file:")
=======
    # Prepare a shell command to open the Colab notebook with parameters
    cmd = f"open -a 'Google Chrome' '{colab_notebook_url}'"
>>>>>>> Stashed changes

    # Execute the shell command to open the notebook
    subprocess.Popen(cmd, shell=True)

st.title("PDF Analysis")

<<<<<<< Updated upstream
            if pdf_library == "PyPDF2":
                # Extract text using PyPDF2
                text = extract_text_pypdf(BytesIO(pdf_content))
                st.subheader("Summary:")
                st.write(text)  # Display the extracted text
            else:
                # Extract text using Nougat
                pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
                text = pdf_base64
                summary = summarize_text_nougat(text)
                st.subheader("Summary:")
                st.write(summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please enter a valid PDF link.")
=======
# Add a radio button to select the PDF processing library
pdf_library = st.radio("Select PDF processing library:", ["PyPDF2", "Nougat"])

# If "Nougat" is selected, hide the text box
if pdf_library == "Nougat":
    st.write("Nougat library selected. No need to enter a link here instead please press the button below")
else:
    # If "PyPDF2" or any other option is selected, show the text box
    pdf_link = st.text_input("Enter the link to the PDF file:")

if pdf_library == "Nougat":
    if st.button("Run Colab Notebook"):
        run_colab_notebook()
        st.success("Colab notebook execution triggered successfully.")

if pdf_library != "Nougat":
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

            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:
            st.warning("Please enter a valid PDF link.")
>>>>>>> Stashed changes
