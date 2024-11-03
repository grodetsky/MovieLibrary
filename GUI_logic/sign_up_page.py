import os
from classes.user import User

def register(username, email, password):
    user = User(name=username, email=email)
    """Password"""

    users = User.load_from_json("users.json") if os.path.exists("users.json") else []
    users.append(user)
    
    User.save_to_json(users, "users.json")
    
    return True

def back_to_login(window, login_window):
    window.destroy() 
    login_window.deiconify()