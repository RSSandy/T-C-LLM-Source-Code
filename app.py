import streamlit as st
import requests
from io import StringIO


# Streamlit app code
st.title("Text File Processing App")

backend_url = "YOUR_BACKEND_URL_HERE"

# File uploader widget
uploaded_file = st.file_uploader("Choose a file to upload", type=["txt", "csv", "jpg", "png", "pdf"])

if uploaded_file is not None:
    # Display the file details
    st.write("File uploaded:", uploaded_file.name)

    # Convert the uploaded file to binary (or base64) to send to the backend
    file_bytes = uploaded_file.read()

    if st.button('Submit'):
        # Send the file to the backend via a POST request
        files = {'file': (uploaded_file.name, file_bytes)}
        response = requests.post(colab_url, files=files)

        # Check the response from the backend
        if response.status_code == 200:
            st.write("File uploaded successfully!")
            st.write(response.json())  # Display backend response
        else:
            st.write("Error with file upload.")

if st.button('Submit'):
    # Send the request to the Google Colab backend
    response = requests.post(colab_url, json={'number': number})
    
    # Check if the request was successful
    if response.status_code == 200:
        result = response.json().get('result')
        st.write(f"The result is: {result}")
    else:
        st.write("Error with the request.")
