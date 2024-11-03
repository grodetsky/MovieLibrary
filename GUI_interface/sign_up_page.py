import customtkinter as ctk 
from GUI_logic.sign_up_page import register, back_to_login

class SignUp(ctk.CTkToplevel):
    def __init__(self, login_window):
        super().__init__()
        
        self.geometry("400x430") 
        self.title("Sign Up")

        frame = ctk.CTkFrame(master=self) 
        frame.pack(pady=20, padx=40, fill='both', expand=True) 

        label_log = ctk.CTkLabel(master=frame, text='Enter your data', font=ctk.CTkFont(size=20)) 
        label_log.pack(pady=12, padx=10) 

        self.name_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.name_entry.pack(pady=12, padx=10)

        self.email_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Email Address')
        self.email_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password')
        self.password_entry.pack(pady=12, padx=10)

        register_button = ctk.CTkButton(master=frame, width=220, text='Register', command=self.open_registration)
        register_button.pack(padx=20, pady=10)

        label_reg = ctk.CTkLabel(master=frame, text='<- Back to Login', font=ctk.CTkFont(size=14, underline=True), cursor="hand2") 
        label_reg.pack(pady=12, padx=10)
        label_reg.bind("<Button-1>", lambda e: back_to_login(self, login_window))  

    def open_registration(self):
        username = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()        
        register(username, email, password)


