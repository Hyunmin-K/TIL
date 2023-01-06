import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
from pprint import pprint

info = ['id','title','vote_average','overview','genre_ids']
movie_info = {}
for i in info:
    movie_info[i] = movie[i]
pprint(movie_info, width=350, sort_dicts=False)