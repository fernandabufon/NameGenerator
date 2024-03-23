import streamlit as st
from helper_langchain import generate_name_and_meaning

st.title("Name Generator")

word = st.text_input('Choose a word, and we will find a name that rhymes with it. Only one word, please!', '')


if word:
    response = generate_name_and_meaning(word)
    st.header(f"The name that rhymes with the word '{word}' is '{response['name'].strip()}'")
    st.write("Meaning :", response['meaning'].strip())