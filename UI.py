import customtkinter as ck
from Calculations import submit
from Tables import table_display
from Charts import chart_display

LEFT_FRAME_COLOR = "#472183"
RIGHT_FRAME_COLOR = "#25164F"
TEXT_COLOR = "#F5F5F5"
BUTTON_COLOR = "#6A1B9A"
HOVER_COLOR = "#7B1FA2"

class LoanApp(ck.CTk):
    def __init__(self):
        super().__init__()

        self.geometry('1200x600')
        self.title('Loan Calculator')

        self.left_frame = ck.CTkFrame(self, fg_color=LEFT_FRAME_COLOR, corner_radius=20)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        title = ck.CTkLabel(self.left_frame, text="Loan Calculator", font=("Arial", 22, "bold"), text_color=TEXT_COLOR)
        title.pack(pady=50)

        self.loan_amt_entry = self.create_label_entry("Enter Loan Amount (€)", pady=20)
        self.loan_int_entry = self.create_label_entry("Enter Loan Interest Rate (%)", pady=20)
        self.loan_tenure_entry = self.create_label_entry("Enter Loan Tenure (Years)", pady=20)

        self.submit_btn = ck.CTkButton(self.left_frame, text="Calculate", font=("Arial", 18, "bold"),
                                       corner_radius=15, fg_color=BUTTON_COLOR, hover_color=HOVER_COLOR,
                                       text_color="white", command=self.calculate)
        self.submit_btn.pack(pady=20, fill="x", padx=10)

        self.right_frame = ck.CTkFrame(self, fg_color=RIGHT_FRAME_COLOR, corner_radius=20)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Résumé
        self.summary_frame = ck.CTkFrame(self.right_frame, fg_color="#3A1C71", corner_radius=15)
        self.summary_frame.pack(fill="x", padx=10, pady=5)

        self.summary_label = ck.CTkLabel(self.summary_frame, text="Loan Summary", font=("Arial", 18, "bold"),
                                         text_color=TEXT_COLOR)
        self.summary_label.pack(pady=5)

        self.summary_text = ck.CTkLabel(self.summary_frame, text="", font=("Arial", 16), wraplength=700,
                                        text_color=TEXT_COLOR)
        self.summary_text.pack()

        # Graphique
        self.chart_frame = ck.CTkFrame(self.right_frame, fg_color=RIGHT_FRAME_COLOR, corner_radius=15)
        self.chart_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Tableau
        self.table_frame = ck.CTkFrame(self.right_frame, fg_color=RIGHT_FRAME_COLOR, corner_radius=15)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    def create_label_entry(self, text, pady=10):
        label = ck.CTkLabel(self.left_frame, text=text, font=("Arial", 16), text_color=TEXT_COLOR)
        label.pack(pady=5)
        entry = ck.CTkEntry(self.left_frame, font=("Arial", 16), fg_color="White", text_color="Black", corner_radius=10)
        entry.pack(pady=pady, fill="x", padx=10)
        return entry

    def calculate(self):
        submit(self.loan_amt_entry, self.loan_int_entry, self.loan_tenure_entry, self.summary_text,
               self.chart_frame, self.table_frame)
