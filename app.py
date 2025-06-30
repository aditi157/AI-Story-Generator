import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_url = "http://127.0.0.1:5000/generate/"

st.set_page_config(page_title="📖 AI Story Generator", layout="centered")
st.title("Story Generator")
st.markdown("Enter a story theme (e.g., *A dragon who learns to bake*)")

theme = st.text_input("Story Theme")

if st.button("Generate Story"):
    if theme.strip():
        with st.spinner("Generating..."):
            res = requests.post(api_url, json={"theme": theme})
            if res.ok:
                story = res.json()["story"]
                st.success("Here's your story:")
                st.write(story)
            else:
                st.error("Story generation failed: " + res.text)
    else:
        st.warning("Please enter a theme.")
