import json

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성 
movie_info = []
for i in range(len(genres_list)):
    # print(genres_list[i])
    # print(movie["genre_ids"])
    for j in range(len(movie["genre_ids"])):
        if movie["genre_ids"][j] == genres_list[i]["id"]:
            movie_info.append(genres_list[i]["name"])
print(movie_info)