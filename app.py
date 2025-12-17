import streamlit as st
import base64
from pathlib import Path

# Set page config
st.set_page_config(page_title="Site Timeline", layout="wide", initial_sidebar_state="collapsed")

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
<style>
{css_content}
</style>

{body_html}

<script>
{js_content}
</script>
"""

# Display using streamlit's html component
st.components.v1.html(full_html, height=2000, scrolling=True)

# Add some padding at the bottom
st.markdown("<br>" * 5, unsafe_allow_html=True)
