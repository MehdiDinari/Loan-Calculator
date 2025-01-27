import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Calculations import submit
from Tables import table_display
from Charts import chart_display

# UI Styling
st.set_page_config(page_title="Loan Calculator", layout="wide")

# Sidebar Input Form
st.sidebar.title("🏦 Loan Calculator")
loan_amt = st.sidebar.number_input("Enter Loan Amount (€)", min_value=0.0, format="%.2f")
loan_int = st.sidebar.number_input("Enter Loan Interest Rate (%)", min_value=0.0, format="%.2f")
loan_tenure = st.sidebar.number_input("Enter Loan Tenure (Years)", min_value=1, format="%d")

# Button to calculate
if st.sidebar.button("📊 Calculate Loan"):
    # Placeholder for summary
    st.subheader("📃 Loan Summary")

    # Call the submit function (assuming it calculates and returns necessary values)
    summary_text, table_data, chart_data = submit(loan_amt, loan_int, loan_tenure)

    # Display Summary in an Expander
    with st.expander("📄 Loan Details", expanded=True):
        st.write(summary_text)

    # Display Chart
    st.subheader("📈 Loan Breakdown Chart")
    fig, ax = plt.subplots()
    chart_display(ax, chart_data)
    st.pyplot(fig)

    # Display Table
    st.subheader("📊 Amortization Table")
    df = pd.DataFrame(table_data)
    st.dataframe(df)

# Footer
st.markdown("---")
st.markdown("🔹 *Built with Streamlit by [Your Name]*")
