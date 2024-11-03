from GUI_interface.sign_up_page import SignUp
import os
from classes.user import User

def login(username, password, window):
    if os.path.exists("users.json"):
        users = User.load_from_json("users.json")
    else:
        users = []
    for user in users:
        if user.get_user_name() == username:
            if password == "123":
                window.destroy()
                return True

def open_registration(self):
    self.withdraw() 
    login_window = self  
    sign_up_window = SignUp(login_window)  
    sign_up_window.grab_set()