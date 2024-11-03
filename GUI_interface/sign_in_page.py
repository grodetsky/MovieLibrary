import customtkinter as ctk 
from GUI_logic.sign_in_page import login
from GUI_interface.home_page import Home

class SignIn(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
    
        self.geometry("400x430") 
        self.title("Log In")

        self.label = ctk.CTkLabel(self, text="Welcome to Movie Library!", font=ctk.CTkFont(size=20, weight="bold")) 
        self.label.pack(pady=20) 

        self.frame = ctk.CTkFrame(master=self) 
        self.frame.pack(pady=20, padx=40, fill='both', expand=True) 

        self.label_log = ctk.CTkLabel(master=self.frame, text='Sign in', font=ctk.CTkFont(size=20)) 
        self.label_log.pack(pady=12, padx=10) 

        self.user_entry = ctk.CTkEntry(master=self.frame, placeholder_text="Username") 
        self.user_entry.pack(pady=12, padx=10) 

        self.user_pass = ctk.CTkEntry(master=self.frame, placeholder_text="Password", show="*") 
        self.user_pass.pack(pady=12, padx=10) 

        self.button = ctk.CTkButton(master=self.frame, text='Login', command=lambda: self.open_login()) 
        self.button.pack(pady=12, padx=10) 

        self.checkbox = ctk.CTkCheckBox(master=self.frame, text='Remember Me') 
        self.checkbox.pack(pady=12, padx=10) 

    def open_login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        if login(username, password, self):
            self.home_window = Home()
            self.home_window.grab_set()
