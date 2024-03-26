import streamlit as st
from helper_langchain import generate_name_and_meaning

st.title("Name Generator")

word = st.text_input('Choose a word, and we will find a name that rhymes with it. Only one word, please!', '')


if word:
    response = generate_name_and_meaning(word)
    if response and 'name' in response and 'meaning' in response:
        name = response['name'].strip()
        meaning = response['meaning'].strip()
        if name and meaning:
            st.header(f"The name that rhymes with the word '{word}' is '{name}'")
            st.write("Meaning:", meaning)
        else:
            st.error("Failed to generate a valid name and meaning. Please try a different word.")
    else:
        st.error("Failed to generate a valid name and meaning. Please try a different word.")
