import streamlit as st
import wireviz.wireviz as wv

with st.form("output options"):
    outpng = st.checkbox("png")
    st.form_submit_button('Save')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write('uploaded!')
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    wv.parse("./temp.txt", "png", "png", "./", "test", "./")

st.write('OR')

with st.form("wireviz text input"):
    st.write('Text input:')
    st.text_area('wireviz file content')
    st.form_submit_button('Submit')
    st.text_area('Preview')
    st.form_submit_button('Download')