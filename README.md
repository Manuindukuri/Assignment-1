# Big Data Systems and Int Analytics - Assignment 1
## Team Information and Contribution 

Name | Email | Contribution 
--- | --- | --- |
Manohar Indukuri | indukuri.k@northeastern.edu | 34%
Prathamesh Kulkarni | kulkarni.prath@northeastern.edu | 33% 
Sarvesh Malpani | 	malpani.sa@northeastern.edu | 33% 

## Project Flow 

### Part 1 :
The workflow for our PDF parsing tool begins with the user interacting with a Streamlit web application. The user has to upload the PDF link and has the choice to select one of two PDF parsing libraries: PyPDF or Nougat. This selection determines the underlying library used for PDF processing. The workflow branches into two distinct paths depending on the user's choice. If the user opts for "PyPDF," the tool calls the function written in Python for PDF parsing while selecting "Nougat" leads to utilizing the Nougat library for the same purpose. Once the parsing is complete, the extracted information is accessible to the user through the Streamlit interface. This final step enables the user to view the parsed PDF content and the generated summary.

### Part 2
The workflow for our Data Quality Evaluation Tool for the Freddie Mac Single-Family Dataset begins with users interacting with a Streamlit web application. Users upload a CSV or XLS file containing Freddie Mac dataset information and specify whether the data is Origination or Monthly performance data. The uploaded data is then processed using the pandas-profiling library and great expectations to provide a summary of the dataset, including statistics, data types, and data distribution, and is displayed on the streamlit dashboard.

## Project Tree 
```
📦 
├─ .DS_Store
├─ .github
│  └─ workflows
│     └─ static.yml
├─ .gitignore
├─ README.md
├─ part_1
│  ├─ .DS_Store
│  ├─ images
│  │  ├─ collab 2.png
│  │  ├─ collab.png
│  │  ├─ greatexpectations.png
│  │  ├─ nougat 2.png
│  │  ├─ nougat.png
│  │  ├─ pandas.png
│  │  ├─ pypdf 2.png
│  │  ├─ pypdf.png
│  │  └─ streamlit.png
│  ├─ main.py
│  ├─ requirements.txt
│  ├─ workflow.py
│  ├─ workflow_diagram
│  └─ workflow_diagram.png
└─ part_2
   ├─ app.py
   ├─ great_expectations
   │  ├─ monthly 2.ipynb
   │  ├─ monthly.ipynb
   │  ├─ orig 2.ipynb
   │  └─ orig.ipynb
   ├─ gx
   │  ├─ .gitignore
   │  ├─ checkpoints
   │  │  ├─ GX_Checkpoint.yml
   │  │  └─ Monthly_Checkpoint.yml
   │  ├─ expectations
   │  │  ├─ .ge_store_backend_id
   │  │  ├─ monthly_performance.json
   │  │  ├─ origin1.json
   │  │  └─ part2.json
   │  ├─ great_expectations 2.yml
   │  ├─ great_expectations.yml
   │  ├─ plugins
   │  │  └─ custom_data_docs
   │  │     └─ styles
   │  │        └─ data_docs_custom_styles.css
   │  └─ uncommitted
   │     ├─ config_variables.yml
   │     ├─ data_docs
   │     │  └─ local_site
   │     │     ├─ expectations
   │     │     │  ├─ monthly_performance.html
   │     │     │  └─ part2.html
   │     │     ├─ index.html
   │     │     ├─ static
   │     │     │  ├─ fonts
   │     │     │  │  └─ HKGrotesk
   │     │     │  │     ├─ HKGrotesk-Bold.otf
   │     │     │  │     ├─ HKGrotesk-BoldItalic.otf
   │     │     │  │     ├─ HKGrotesk-Italic.otf
   │     │     │  │     ├─ HKGrotesk-Light.otf
   │     │     │  │     ├─ HKGrotesk-LightItalic.otf
   │     │     │  │     ├─ HKGrotesk-Medium.otf
   │     │     │  │     ├─ HKGrotesk-MediumItalic.otf
   │     │     │  │     ├─ HKGrotesk-Regular.otf
   │     │     │  │     ├─ HKGrotesk-SemiBold.otf
   │     │     │  │     └─ HKGrotesk-SemiBoldItalic.otf
   │     │     │  ├─ images
   │     │     │  │  ├─ favicon.ico
   │     │     │  │  ├─ glossary_scroller.gif
   │     │     │  │  ├─ iterative-dev-loop.png
   │     │     │  │  ├─ logo-long-vector.svg
   │     │     │  │  ├─ logo-long.png
   │     │     │  │  ├─ short-logo-vector.svg
   │     │     │  │  ├─ short-logo.png
   │     │     │  │  └─ validation_failed_unexpected_values.gif
   │     │     │  └─ styles
   │     │     │     ├─ data_docs_custom_styles_template.css
   │     │     │     └─ data_docs_default_styles.css
   │     │     └─ validations
   │     │        ├─ monthly_performance
   │     │        │  └─ Monthly_run
   │     │        │     ├─ 20231006T011054.523840Z
   │     │        │     │  └─ File2-Asset2.html
   │     │        │     └─ 20231006T014748.723102Z
   │     │        │        └─ Monthly-Asset1.html
   │     │        └─ part2
   │     │           └─ Manual_run7
   │     │              └─ 20231005T153120.852569Z
   │     │                 └─ File-Asset.html
   │     └─ validations
   │        ├─ .ge_store_backend_id
   │        ├─ monthly_performance
   │        │  └─ Monthly_run
   │        │     ├─ 20231006T011054.523840Z
   │        │     │  └─ File2-Asset2.json
   │        │     └─ 20231006T014748.723102Z
   │        │        └─ Monthly-Asset1.json
   │        └─ part2
   │           └─ Manual_run7
   │              └─ 20231005T153120.852569Z
   │                 └─ File-Asset.json
   ├─ main.py
   ├─ output.csv
   ├─ output3.csv
   ├─ requirements.txt
   └─ streamlit
      └─ .streamlit
         ├─ bin
         │  ├─ Activate.ps1
         │  ├─ activate
         │  ├─ activate.csh
         │  ├─ activate.fish
         │  ├─ pip
         │  ├─ pip3
         │  ├─ pip3.11
         │  ├─ python
         │  ├─ python3
         │  └─ python3.11
         └─ pyvenv.cfg
```
## Link to the Live Applications
- Streamlit Application (Part 1): https://bigdataia-fall2023-team-1-assignment-1-part-1main-c4hiku.streamlit.app/
- Streamlit Application (Part 2): https://bigdataia-fall2023-team-1-assignment-1-part-2main-ijfadp.streamlit.app/

## Link to Codelab
- Part 1 : https://codelabs-preview.appspot.com/?file_id=1bWkZdGurOufpXn0ausMuI0dNQvnJ_OxzVsDwUWmHMqU#0
- Part 2 : https://codelabs-preview.appspot.com/?file_id=1unCqMpXiX_hpSKtdzLZ9OyGHscLuEF-JqEr6hojCUCQ#0
