class Favorite_Movie():
    """Class to provide API for getting list of favorite movies"""
    def __init__(self):
        self.movies = [
        ('Toy Story',
        'Story Aout Toys',
        'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450',
        'https://www.youtube.com/watch?v=KYz2wyBy3kc', '1995'),
        ('Ten Years',
        '5 short stories of Hong Kong after ten years',
        'https://cdn.thestandnews.com/media/photos/cache/C2ABE58D81E5B9B4C2BB2020TEN20YEARS202012376056_562681027217993_303987522533359407_n_1024_xnYjN_1200x0.jpg',
        'https://www.youtube.com/watch?v=M4zebygSaZE', '2016'),
        ('Spotlight',
        'The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.',
        'http://i1.wp.com/teaser-trailer.com/wp-content/uploads/Spotlight-Poster-1.jpg',
        'https://www.youtube.com/watch?v=tb_WgKDqPsE', '2015'),
        ('Moulin Rouge',
        'A poet falls for a beautiful courtesan whom a jealous duke covets in this stylish musical, with music drawn from familiar 20th century sources.',
        'http://straypoetry.com/wp-content/uploads/2012/03/MPW-15376.jpeg',
        'https://www.youtube.com/watch?v=dMSvKpVwavk', '2001'),
        ('Toy Story',
        'Story Aout Toys',
        'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450',
        'https://www.youtube.com/watch?v=KYz2wyBy3kc', '1995'),
        ('Ten Years',
        '5 short stories of Hong Kong after ten years',
        'https://cdn.thestandnews.com/media/photos/cache/C2ABE58D81E5B9B4C2BB2020TEN20YEARS202012376056_562681027217993_303987522533359407_n_1024_xnYjN_1200x0.jpg',
        'https://www.youtube.com/watch?v=M4zebygSaZE', '2016'),
        ('Spotlight',
        'The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.',
        'http://i1.wp.com/teaser-trailer.com/wp-content/uploads/Spotlight-Poster-1.jpg',
        'https://www.youtube.com/watch?v=tb_WgKDqPsE', '2015'),
        ('Moulin Rouge',
        'A poet falls for a beautiful courtesan whom a jealous duke covets in this stylish musical, with music drawn from familiar 20th century sources.',
        'http://straypoetry.com/wp-content/uploads/2012/03/MPW-15376.jpeg',
        'https://www.youtube.com/watch?v=dMSvKpVwavk', '2001'),
        ('Toy Story',
        'Story Aout Toys',
        'http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450',
        'https://www.youtube.com/watch?v=KYz2wyBy3kc', '1995'),
        ('Ten Years',
        '5 short stories of Hong Kong after ten years',
        'https://cdn.thestandnews.com/media/photos/cache/C2ABE58D81E5B9B4C2BB2020TEN20YEARS202012376056_562681027217993_303987522533359407_n_1024_xnYjN_1200x0.jpg',
        'https://www.youtube.com/watch?v=M4zebygSaZE', '2016'),
        ('Spotlight',
        'The true story of how the Boston Globe uncovered the massive scandal of child molestation and cover-up within the local Catholic Archdiocese, shaking the entire Catholic Church to its core.',
        'http://i1.wp.com/teaser-trailer.com/wp-content/uploads/Spotlight-Poster-1.jpg',
        'https://www.youtube.com/watch?v=tb_WgKDqPsE', '2015'),
        ('Moulin Rouge',
        'A poet falls for a beautiful courtesan whom a jealous duke covets in this stylish musical, with music drawn from familiar 20th century sources.',
        'http://straypoetry.com/wp-content/uploads/2012/03/MPW-15376.jpeg',
        'https://www.youtube.com/watch?v=dMSvKpVwavk', '2001'),
        ]

    def get_favorite_movies(self):
        return self.movies

    def get_favorite_movies_by_year(self, year):
        result = []
        for movie in self.movies:
            if year in movie[4]:
                result.append(movie)
        return result
