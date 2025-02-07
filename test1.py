import streamlit as st
import wireviz.wireviz as wvasdf

st.write('Wireviz YAML to PNG')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    output = wvasdf.parse(inp=("C:/Users/jeffrey/Documents/GitHub/wireviz-streamlit/temp.txt"), output_formats=("png"), return_types=("png"))
    st.write('Preview:')
    st.image(output)
    st.download_button("Download image file", output, "output.png")