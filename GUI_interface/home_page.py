import customtkinter as ctk 

class Home(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.title("Movie Library")
        self.geometry("1000x530")
        self.label = ctk.CTkLabel(self, text="Welcome!!!", font=ctk.CTkFont(size=50, weight="bold")) 
        self.label.pack(pady=20)