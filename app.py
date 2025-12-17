import streamlit as st
import base64
from pathlib import Path

# Set page config
st.set_page_config(page_title="Site Timeline", layout="wide", initial_sidebar_state="collapsed")

# Set background color
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #0e1117;
        }
        [data-testid="stHeader"] {
            background-color: #0e1117;
        }
    </style>
""", unsafe_allow_html=True)

# Read CSS file
with open("style.css", "r") as f:
    css_content = f.read()

# Read JavaScript file
with open("script.js", "r") as f:
    js_content = f.read()

# Read HTML file
with open("index.html", "r") as f:
    html_content = f.read()

# Extract the body content from HTML (between <body> and </body>)
body_start = html_content.find("<body>") + 6
body_end = html_content.find("</body>")
body_html = html_content[body_start:body_end]

# Function to convert image files to base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# Prepare inline HTML/CSS/JS with embedded images
full_html = f"""
<!DOCTYPE html>
<html style="overflow-x: auto; overflow-y: auto;">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap" rel="stylesheet">
<style>
html {{
  overflow-x: auto;
  overflow-y: auto;
  scrollbar-width: none;
}}
html::-webkit-scrollbar {{
  display: none;
}}
body {{
  overflow-x: auto;
  overflow-y: auto;
  margin: 0;
  padding: 0;
  background-color: #0e1117;
  scrollbar-width: none;
}}
body::-webkit-scrollbar {{
  display: none;
}}
{css_content}
</style>
</head>
<body style="overflow-x: auto; overflow-y: auto;">
{body_html}

<script>
{js_content}
</script>
</body>
</html>
"""

# Display using streamlit's html component
st.components.v1.html(full_html, height=800, scrolling=True)
