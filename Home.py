import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=600)

with col2:
    st.title("Miro")
    content = """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi cursus est ut tellus congue, eget tincidunt nisl fringilla.
             Integer ipsum lectus, rutrum et erat id, efficitur laoreet mauris. Ut porttitor bibendum magna hendrerit commodo. 
             Maecenas porta, ligula in finibus elementum, lacus augue egestas libero, vitae eleifend quam nibh sed turpis. 
             Nullam pulvinar mi velit, eu vestibulum lectus vehicula vitae. 
             Fusce semper viverra quam, non auctor eros facilisis at. Sed tristique elit vel sapien bibendum venenatis. 
    """
    st.info(content)

content2 = """
   some random text 
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
