import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def chart_display(frame, principal, total_interest):
    for widget in frame.winfo_children():
        widget.destroy()

    fig = plt.Figure(figsize=(6, 3), dpi=100)
    plot = fig.add_subplot(111)
    values = [principal, total_interest]
    labels = ['Principal', 'Total Interest']
    plot.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, explode=[0.0, 0.1],
             colors=["#7E57C2", "#E91E63"])
    plot.set_title("Loan Breakdown")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()
