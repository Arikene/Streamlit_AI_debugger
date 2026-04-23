import streamlit as st
from google import genai
import os
from api_calling import generate_response
from PIL import Image


st.title("Your AI Code Debugger", anchor=False)
st.markdown("Upload upto 3 screenshots of your code and the error message, and let the AI Code Debugger analyze them to provide you with insights and potential solutions.")

st.divider()

with st.sidebar:
    st.header("How to Use")
    st.markdown(
        """
        1. Upload screenshots of your code and the error message (up to 3 images).
        2. Click the 'Analyze' button to let the AI Code Debugger process the images.
        3. View the generated insights and potential solutions based on the uploaded screenshots.
        """
    )
    images = st.file_uploader("Upload your code screenshots", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
pil_images = []

if images:
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)

if pil_images:
    if len(pil_images) > 3:
        st.warning("Please upload a maximum of 3 images.")
    else:
        st.subheader("Uploaded Images")
        col = st.columns(len(pil_images))

        for i, pil_image in enumerate(pil_images):
            with col[i]:
                st.image(pil_image, caption=f"Image {i+1}", use_column_width=True)


button = st.button("Debug Code")

if button:
    if not pil_images:
        st.warning("Please upload at least one image to analyze.")
    else:
        with st.container(border=True)        :
            st.subheader("AI Code Debugger Insights")
            
            #creating a spinner
            with st.spinner("Debugging your code..."):
                response = generate_response(pil_images)
                st.markdown(response)



