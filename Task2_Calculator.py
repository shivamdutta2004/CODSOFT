# Shivam Dutta
# CODSOFT Internship - Task 2: Calculator (Enhanced UI)

import streamlit as st

# Page config
st.set_page_config(page_title="Calculator", layout="centered")

# Custom styling (🔥 makes it look premium)
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
    }
    .result-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #1f6f43;
        color: white;
        font-size: 18px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'>🧮 Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Perform quick and accurate calculations</p>", unsafe_allow_html=True)

st.write("---")

# Input layout (side by side)
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

# Operation selection
operation = st.selectbox(
    "Select Operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate Result"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (×)":
        result = num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"

    # Result display (🔥 styled)
    st.markdown(f"<div class='result-box'>Result: {result}</div>", unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("Developed by Shivam Dutta | CODSOFT Internship")