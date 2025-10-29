import datetime

class Movie:
    def __init__(self, movieId: int, title: str, genres: list[str]):
        self.movieId = movieId
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movieId: int, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId: int, movieId: int, rating: float, timestamp: datetime ):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp
        
class Tag:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.rating = tag
        self.timestamp = timestamp