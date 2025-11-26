from pydantic import BaseModel

class Link(BaseModel):
    movieId: int
    imdbId: int
    tmdbId: int

