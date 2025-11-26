import csv
from api.schemas.movie import Movie
from api.schemas.link import Link
from api.schemas.rating import Rating
from api.schemas.tag import Tag

def load_csv(file_path: str):
    data_list = []
    with open(file_path, newline='', mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_list.append(row)
    return data_list

def get_all_movies():
    raw_data = load_csv("data/movies.csv") 
    return [Movie(**row) for row in raw_data]

def get_all_links(path: str = "data/links.csv"):
    raw_data = load_csv(path)
    return [Link(**row) for row in raw_data]

def get_all_ratings(path: str = "data/ratings.csv"):
    raw_data = load_csv(path)
    return [Rating(**row) for row in raw_data]

def get_all_tags(path: str = "data/tags.csv"):
    raw_data = load_csv(path)
    return [Tag(**row) for row in raw_data]