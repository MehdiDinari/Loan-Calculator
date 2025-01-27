import customtkinter as ck
from UI import LoanApp

if __name__ == "__main__":
    ck.set_appearance_mode('dark')
    ck.set_default_color_theme('blue')

    app = LoanApp()
    app.mainloop()
