import media
import my_favorite
import fresh_tomatoes

movies = []
my_favorite = my_favorite.Favorite_Movie()

# Get all favorite movies
favorite_movies = my_favorite.get_favorite_movies()

# Get Moulin Rouge only
# favorite_movies = my_favorite.get_favorite_movies_by_year('2001')

# Get Toy Story only
# favorite_movies = my_favorite.get_favorite_movies_by_year('1995')

# Get Ten Years only
# favorite_movies = my_favorite.get_favorite_movies_by_year('2016')

# Get Spotlight only
# favorite_movies = my_favorite.get_favorite_movies_by_year('2015')

for movie in favorite_movies:
    movies.append(media.Movie(movie[0], movie[1], movie[2], movie[3], movie[4]))

fresh_tomatoes.open_movies_page(movies)
