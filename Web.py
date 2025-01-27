import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# UI Styling
st.set_page_config(page_title="Loan Calculator", layout="wide")

# Sidebar Input Form
st.sidebar.title("🏦 Loan Calculator")
loan_amt = st.sidebar.number_input("Enter Loan Amount (€)", min_value=0.0, format="%.2f")
loan_int = st.sidebar.number_input("Enter Loan Interest Rate (%)", min_value=0.0, format="%.2f")
loan_tenure = st.sidebar.number_input("Enter Loan Tenure (Years)", min_value=1, format="%d")

# Function to calculate loan schedule and EMI
def calculate_loan(p, i, t):
    roi_per_mon = i / 12 / 100
    tenure_in_mon = t * 12
    emi = (p * roi_per_mon * pow(1 + roi_per_mon, tenure_in_mon)) / (pow(1 + roi_per_mon, tenure_in_mon) - 1)
    balance = p
    total_interest = 0
    schedule = []

    for mon in range(tenure_in_mon):
        interest_monthly_payable = balance * roi_per_mon
        remain_emi_bal = emi - interest_monthly_payable
        balance -= remain_emi_bal
        total_interest += interest_monthly_payable
        schedule.append({
            'Month': mon + 1,
            'Interest Paid (€)': round(interest_monthly_payable, 2),
            'Principal Paid (€)': round(remain_emi_bal, 2),
            'EMI (€)': round(emi, 2),
            'Remaining Balance (€)': round(balance, 2)
        })

    return pd.DataFrame(schedule), total_interest, round(emi, 2)

# Function to generate pie chart
def chart_display(principal, total_interest):
    fig, ax = plt.subplots(figsize=(6, 3))
    values = [principal, total_interest]
    labels = ['Principal', 'Total Interest']
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, explode=[0.0, 0.1],
           colors=["#7E57C2", "#E91E63"])
    ax.set_title("Loan Breakdown")
    return fig

# Button to calculate
if st.sidebar.button("📊 Calculate Loan"):
    if loan_amt > 0 and loan_int > 0 and loan_tenure > 0:
        # Perform loan calculations
        df, total_interest, emi = calculate_loan(loan_amt, loan_int, loan_tenure)

        # Display Loan Summary
        with st.expander("📄 Loan Details", expanded=True):
            st.write(f"""
            - **Loan Amount:** €{loan_amt:,.2f}
            - **Interest Rate:** {loan_int:.2f}%
            - **EMI:** €{emi:,.2f}
            - **Tenure:** {loan_tenure} years
            - **Total Interest Paid:** €{total_interest:,.2f}
            """)

        # Display Chart
        st.subheader("📈 Loan Breakdown Chart")
        fig = chart_display(loan_amt, total_interest)
        st.pyplot(fig)

        # Display Table
        st.subheader("📊 Amortization Table")
        st.dataframe(df)
    else:
        st.error("⚠ Please enter valid values for loan calculation!")

# Footer
st.markdown("---")
st.markdown("🔹 *Built with Streamlit by [Mehdi Dinari]*")
