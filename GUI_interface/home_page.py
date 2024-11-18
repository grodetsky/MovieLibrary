import customtkinter as ctk
from GUI_logic.home_page import show_account_info, show_movies_info

class Home(ctk.CTkToplevel):
    def __init__(self, username):
        super().__init__()

        self.username = username

        self.title("Movie Library")
        self.geometry("1000x530")

        self.grid_columnconfigure(1, weight=1) 
        self.grid_columnconfigure(2, weight=0)  
        self.grid_rowconfigure(0, weight=1)  

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)  
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew") 
        self.sidebar_frame.grid_rowconfigure(4, weight=1)  

        self.user_label = ctk.CTkLabel(self.sidebar_frame, text=f"Welcome, {self.username}!", font=ctk.CTkFont(size=20, weight="bold"))
        self.user_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Account", command=self.show_account_info)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10) 

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Movies", command=self.show_movies_info)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.main_content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_content_frame.grid(row=0, column=1, sticky="nsew")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_movies_info()  

    def show_account_info(self):
        """Account page"""
        account_info = show_account_info(self.username)  

        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        if account_info:
            title_label = ctk.CTkLabel(self.main_content_frame, text="User Information", font=ctk.CTkFont(size=20, weight="bold"))
            title_label.grid(row=0, column=1, padx=20, pady=10)

            row = 1
            for key, value in account_info.items():
                info_label = ctk.CTkLabel(self.main_content_frame, text=f"{key.capitalize()}: {value}",
                                          font=ctk.CTkFont(size=15))
                info_label.grid(row=row, column=1, padx=20, pady=5)
                row += 1
        else:
            error_label = ctk.CTkLabel(self.main_content_frame, text="No user data found.", font=ctk.CTkFont(size=15, weight="bold"))
            error_label.grid(row=0, column=1, padx=20, pady=10)

    def show_movies_info(self):
        """Movie page"""
        for widget in self.main_content_frame.winfo_children():
            widget.destroy()

        title_label = ctk.CTkLabel(self.main_content_frame, text="Top Movies", font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(10, 5))

        scrollable_frame = ctk.CTkScrollableFrame(self.main_content_frame, width=900, height=400)
        scrollable_frame.pack(pady=10, padx=20, fill="both", expand=True)

        movies = show_movies_info()

        if movies:
            row = 0
            for movie in movies:
                movie_title_label = ctk.CTkLabel(scrollable_frame, text=f"Title: {movie.get_movie_title()}", font=ctk.CTkFont(size=15))
                movie_title_label.grid(row=row, column=0, padx=20, pady=5, sticky="w")

                movie_info_label = ctk.CTkLabel(
                    scrollable_frame,
                    text=f"Director: {movie.get_movie_director()} | Year: {movie.get_release_year()} | Genre: {movie.get_genre()} | Rating: {movie.get_rating()}", font=ctk.CTkFont(size=13)
                )
                movie_info_label.grid(row=row, column=1, padx=20, pady=5, sticky="w")
                row += 1
        else:
            no_movies_label = ctk.CTkLabel(scrollable_frame, text="No movies found.", font=ctk.CTkFont(size=15, weight="bold"))
            no_movies_label.grid(row=0, column=0, padx=20, pady=10)