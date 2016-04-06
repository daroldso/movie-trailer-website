import media
import my_favorite
import fresh_tomatoes

favorite_movies = my_favorite.Favorite_Movie().get_favorite_movies()
movies = []

for movie in favorite_movies:
    movies.append(media.Movie(movie[0], movie[1], movie[2], movie[3], movie[4]))

fresh_tomatoes.open_movies_page(movies)