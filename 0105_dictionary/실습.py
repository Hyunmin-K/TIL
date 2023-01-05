# 문제 1
# line = input("문자열을 입력하세요 > ")
# cnt = 0
# for word in line:
#     if word == "e":
#         cnt = cnt+1
# print(cnt)

# 문제 2
# cnt = 0
# line = input("문자열을 입력하세요 > ")
# vowel = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
# for word in line:
#     if word in vowel:
#         cnt = cnt+1
# print(cnt)

# 문제 3
# dict_variable = {
#     "이름":"정우영", 
#     "생년":"2000",
#     "회사":"하이퍼그로스",
# }
# age = 2024 - int(dict_variable["생년"])
# print(f"나이 : {age}세")

# 문제 4
# name = input("이름을 입력하세요 > ")
# phone = input("전화번호를 입력하세요 > ")
# address = input("거주지를 입력하세요 > ")
# dict_variable = {
#     "이름":name,
#     "전화번호":phone,
#     "거주지":address
# }
# print(dict_variable)
# for key,value in dict_variable.items():
#     print(f"{key} : {value}")

# 문제 5
# name = input("이름을 입력하세요 > ")
# phone = input("전화번호를 입력하세요 > ")
# mail = input("이메일을 입력하세요 > ")
# address = input("거주지를 입력하세요 > ")

# dict_name = {"이름":name}
# dict_variable = {
#     "전화번호":phone,
#     "이메일":mail,
#     "거주지":address
# }
# dict_inform = {dict_name["이름"]:dict_variable}
# print(dict_inform)

# 문제 6
line = input("문자열을 입력하세요 > ")
dict_word = {}
for word in line:
    cnt = 0
    for i in line:
        if word == i:
            cnt = cnt+1
    dict_word[word]= cnt
for answer_key, answer_value in dict_word.items():
    print(answer_key, answer_value)