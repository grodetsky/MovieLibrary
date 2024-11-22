import os
from classes.user import User
from classes.movie import Movie

def show_account_info(username):
    """Account page"""
    if os.path.exists("users.json"):
        users_list = User.load_from_json("users.json")
        users_dict = {user.get_user_name(): user for user in users_list}
        user_data = users_dict.get(username, None)

        if user_data:
            user_dict = user_data.to_dict()
            if "added_movies" in user_dict:
                user_dict["added_movies"] = ", ".join(movie["title"] for movie in user_dict["added_movies"])
            return user_dict
    return None

def show_movies_info():
    """Movies page"""
    if os.path.exists("movies.json"):
        movies = Movie.load_from_json("movies.json")
        return movies
    return []