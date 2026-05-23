# Shivam Dutta
# CODSOFT Internship - Task 3: Password Generator

import streamlit as st
import random
import string

st.set_page_config(page_title="Password Generator", layout="centered")

# Title
st.title("🔐 Password Generator")
st.write("Generate strong and secure passwords instantly.")

st.write("---")

# User inputs
length = st.slider("Select password length", 4, 20, 8)

col1, col2 = st.columns(2)

with col1:
    use_digits = st.checkbox("Include Numbers")

with col2:
    use_symbols = st.checkbox("Include Symbols")

# Generate password
if st.button("Generate Password"):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    st.success(f"Generated Password: {password}")

st.write("---")
st.caption("Developed by Shivam Dutta | CODSOFT Internship")