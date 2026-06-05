import streamlit as st
st.title("Hello Streamlit!")

# Text input
name = st.text_input("Enter your name")

# Button interaction
if st.button("Greet me"):
        st.write(f"Hello, {name}!")

# Choose acolor
color = st.selectbox("Pick a color", ["Red", "Green", "Blue"])

st.write(f"You chose: {color}")

# Simple slider
value = st.slider("Pick a number", 0, 100)

st.write(f"Number selected: {value}")