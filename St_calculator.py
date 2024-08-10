def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        print("Invalid")
    return a/b
def square(a):
    return a * a

import streamlit as st

# Title of the application
st.title("Welcome to Scientific Calculator")

# Subheader
st.subheader("By Taqdees Shahzad")

# Create a sidebar for user input
st.sidebar.header("Choose an Operation")
operation = st.sidebar.selectbox(
    "Select the Function",
    ["Addition", "Subtraction", "Multiplication", "Division", "Square"]
)

# Get user input for the numbers
num1 = None
num2 = None
if operation != "Square":
    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")
else:
    num1 = st.number_input("Enter number:", format="%.2f")

# Perform the calculation based on user input
if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        try:
            result = divide(num1, num2)
        except ValueError as e:
            st.error(e)
            result = None
    elif operation == "Square":
        result = square(num1)

    if result is not None:
        st.success(f"The result is: {result}")

# Style the application
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        color: #333;
        font-family: 'Arial', sans-serif;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #e6e6e6;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)