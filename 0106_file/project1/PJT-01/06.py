import json

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
from pprint import pprint
info = ['id','title','poster_path','vote_average','overview','genre_ids']

collect = []
for i in range(20):
    movie_info = {}
    for inform in info:
        movie_info[inform] = (movies_list[i][inform])

    collect.append(movie_info)
pprint(collect, width=350, sort_dicts=False)