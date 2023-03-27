from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        else:
            return False

    def __check_if_is_the_owner_of_the_movie(self, username, movie):
        for user in self.users_collection:
            if user.username == username:
                if user.username == movie.owner.username:
                    return True
                else:
                    return False

    def __check_if_movie_is_uploaded(self, movie):
        for m in self.movies_collection:
            if m.title == movie.title:
                return True
        else:
            return False

    def __check_if_user_liked_the_movie(self, username, movie):
        for user in self.users_collection:
            if user.username == username:
                for m in user.movies_liked:
                    if m.title == movie.title:
                        return True
                else:
                    return False

    def register_user(self, username: str, age: int):
        if self.__check_if_user_exists(username):
            raise Exception("User already exists!")
        else:
            self.users_collection.append(User(username, age))
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        if not self.__check_if_user_exists(username):
            raise Exception("This user does not exist!")
        elif not self.__check_if_is_the_owner_of_the_movie(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        elif self.__check_if_movie_is_uploaded(movie):
            raise Exception("Movie already added to the collection!")
        else:
            user = [u for u in self.users_collection if u.username == username][0]
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
            return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__check_if_movie_is_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not self.__check_if_is_the_owner_of_the_movie(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        else:
            for key, value in kwargs.items():
                setattr(movie, key, value)
            return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not self.__check_if_movie_is_uploaded(movie):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        elif not self.__check_if_is_the_owner_of_the_movie(username, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        else:
            user = [u for u in self.users_collection if u.username == username][0]
            user.movies_owned.remove(movie)
            self.movies_collection.remove(movie)
            return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if self.__check_if_is_the_owner_of_the_movie(username, movie):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        elif self.__check_if_user_liked_the_movie(username, movie):
            raise Exception(f"{username} already liked the movie {movie.title}!")
        else:
            movie.likes += 1
            user = [u for u in self.users_collection if u.username == username][0]
            user.movies_liked.append(movie)
            return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        if not self.__check_if_user_liked_the_movie(username, movie):
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        else:
            movie.likes -= 1
            user = [u for u in self.users_collection if u.username == username][0]
            user.movies_liked.remove(movie)
            return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            sorted_details = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                sorted_details.append(movie.details())
            return "\n".join(sorted_details)

    def __str__(self):
        result = ''
        if self.users_collection:
            result += f"All users: {', '.join(x.username for x in self.users_collection)}\n"
        else:
            result += "All users: No users.\n"

        if self.movies_collection:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}"
        else:
            result += "All movies: No movies."

        return result
