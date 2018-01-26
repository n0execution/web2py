import requests
import json

def index():
    return dict()

def grab_movies():
    session.m = []
    YOUR_OWN_KEY = 'GET_YOUR_OWN_KEY'
    url = requests.get("http://api.rottentomatoes.com/api/public/v1.0/" + "lists/movies/in_theaters.json?apikey={}".format(YOUR_OWN_KEY))
    binary = url.content
    output = json.loads(binary)
    movies = output['movies']
    for movie in movies:
        session.m.append(movie["title"])
    session.m.sort()
    return TABLE(*[TR(v) for v in session.m]).xml()
