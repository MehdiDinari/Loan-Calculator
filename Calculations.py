import pandas as pd
from Tables import table_display
from Charts import chart_display

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
            'Interest': round(interest_monthly_payable, 2),
            'Principle Payable': round(remain_emi_bal, 2),
            'EMI': round(emi, 2),
            'Balance Principle': round(balance, 2)
        })

    return pd.DataFrame(schedule), p, total_interest, round(emi, 2)

def submit(loan_amt_entry, loan_int_entry, loan_tenure_entry, summary_text, chart_frame, table_frame):
    try:
        principal = float(loan_amt_entry.get())
        interest = float(loan_int_entry.get())
        tenure = int(loan_tenure_entry.get())

        data, p, total_interest, emi = calculate_loan(principal, interest, tenure)

        table_display(table_frame, data)
        chart_display(chart_frame, principal, total_interest)
        summary_text.configure(text=f"""
Loan Amount: {p:,.2f} €
Interest Rate: {interest:.2f}%
EMI: {emi:,.2f} €
Tenure: {tenure} years
Total Interest: {total_interest:,.2f} €
        """)
    except ValueError:
        summary_text.configure(text="⚠ Please enter valid numerical values!", text_color="red")
