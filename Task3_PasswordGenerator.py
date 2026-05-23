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

col1, col2, col3 = st.columns(3)

with col1:
    use_upper = st.checkbox("Include Uppercase", value=True)

with col2:
    use_digits = st.checkbox("Include Numbers")

with col3:
    use_symbols = st.checkbox("Include Symbols")

# Generate password
if st.button("Generate Password"):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))

    st.success(f"Generated Password: {password}")

    # ------------------ Strength Indicator ------------------
    strength = "Weak ⚠"
    
    if length >= 12 and use_digits and use_symbols and use_upper:
        strength = "Strong 💪"
    elif length >= 8:
        strength = "Medium ⚡"

    st.info(f"Password Strength: {strength}")

st.write("---")
st.caption("Developed by Shivam Dutta | CODSOFT Internship")
