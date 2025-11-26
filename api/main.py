from fastapi import FastAPI
from .endpoints import links, movies, ratings, tags
app = FastAPI()

app.include_router(links.router)
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(tags.router)
@app.get("/")
def read_root():
    return {"Hello": "World"}


