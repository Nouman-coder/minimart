import streamlit as st

st.set_page_config(page_title="Mini Mart", page_icon="🛒")
st.title("🛒 Welcome to Mini Mart!")


products = {
    "Apples": "$2 per kg",
    "Bread": "$1.5 per loaf",
    "Milk": "$1.2 per liter",
    "Eggs": "$3 per dozen"
}


product_choice = st.selectbox("Select a product to buy:", list(products.keys()))


if st.button("Show Price"):
    price = products[product_choice]
    st.success(f"You selected **{product_choice}**. Price: **{price}**.")