import streamlit as st
import wireviz.wireviz as wv

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write('uploaded!')
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.getbuffer())
    wv.parse("./temp.txt")

with st.form("my_form"):
    st.text_area('wireviz file content')
    st.form_submit_button('Submit')
    st.text_area('Preview')
    st.form_submit_button('Download')