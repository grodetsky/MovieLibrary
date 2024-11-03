import customtkinter as ctk
from GUI_interface.sign_in_page import SignIn 

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Movie Library")
        self.geometry("1000x530") 
        self.withdraw()
        self.sign_in_window = SignIn()
        self.sign_in_window.grab_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()