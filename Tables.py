from tkinter import ttk

def table_display(frame, data):
    for widget in frame.winfo_children():
        widget.destroy()

    table = ttk.Treeview(frame, columns=('Month', 'Interest', 'Principle Payable', 'EMI', 'Balance Principle'), show='headings')

    for col in table["columns"]:
        table.heading(col, text=col)
        table.column(col, anchor="center")

    for _, row in data.iterrows():
        table.insert("", "end", values=tuple(row))

    table.pack(fill="both", expand=True)
