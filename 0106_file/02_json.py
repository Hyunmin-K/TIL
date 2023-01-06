import json
with open('0106_FILE/movie.json','r',encoding='UTF8') as f:
    movie = json.load(f)
    print(movie)