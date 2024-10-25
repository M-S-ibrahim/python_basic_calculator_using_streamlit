import streamlit as st

st.title("PYTHON CALCULATOR")

# Input for operation
Expr = st.text_input("Enter Your Operation (-, +, *, /):")

# Input for first and second numbers
Input1 = st.text_input("Enter Your First Number:")
Input2 = st.text_input("Enter Your Second Number:")

# Ensure the calculation happens when the button is pressed
if st.button("Result"):
    try:
        # Convert inputs to float for calculation
        num1 = float(Input1)
        num2 = float(Input2)
        
        # Perform the calculation based on the operation
        if Expr == "+":
            result = num1 + num2
            st.write("Result: You Add:", result)
        elif Expr == "-":
            result = num1 - num2
            st.write("Result: You Subtract:", result)
        elif Expr == "/":
            if num2 != 0:
                result = num1 / num2
                st.write("Result: You Divide:", result)
            else:
                st.write("Error: Division by Zero")
        elif Expr == "*":
            result = num1 * num2
            st.write("Result: You Multiply:", result)
        else:
            st.write("Invalid operation. Please enter one of: +, -, *, /")
    except ValueError:
        st.write("Invalid input: Please enter numeric values for both numbers.")
