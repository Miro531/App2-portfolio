import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("Miro")
    content = """
    Hi there everyone my name is Miro I'am an adveturist an tech entusiast
    """
    st.write(content)