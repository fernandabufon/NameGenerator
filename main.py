import streamlit as st
from helper_langchain import generate_restaurant_name_and_items

st.title("Restaurant Name")

cuisine = st.sidebar.selectbox("Pick a Cuisin", ("Brazilian", "Arabic", "Indian", "Mexican", "American"))


if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("Menu Items:")
    for item in menu_items:
        st.write("-", item)