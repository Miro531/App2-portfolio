import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("Miro")
    content = """
    Hi there everyone my name is Miro I'am an adveturist an tech entusiast based in Italy. Currently I'am deeping in my knowledge 
    in Python, Red hat administration and AWS in order to get certified. This site is a showcase of some applications and web applications I created as
    a portafolio.
    """
    st.info(content)

content2 = """
   some random text 
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])