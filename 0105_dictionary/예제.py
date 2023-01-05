# 예제 1
# dict_variable = {}
# dict_variable["이름"] = "정우영"
# dict_variable["생년월일"] = "19000101"
# dict_variable["회사"] = "하이퍼그로스"

# print(dict_variable["이름"]) # 정우영
# print(dict_variable["생년월일"]) # 19000101
# print(dict_variable["회사"]) # 하이퍼그로스

# 예제 2
# dict_variable = {"a" : "A", "B" : "b"}
# dict_variable["c"] = "C"
# dict_variable["D"] = "d"
# dict_variable["e"] = "E"

# print(dict_variable["a"]) # A
# print(dict_variable["D"]) # d
# print(dict_variable["b"]) # 오류 : key값 없음

# 예제 3
# dict_variable = {}
# dict_variable["apple"] = 5000
# dict_variable["banana"] = 3000
# dict_variable["apple"] = 2000
# dict_variable["banana"] = dict_variable["banana"] + 1000
# print(dict_variable["apple"] + dict_variable["banana"]) # 6000

# 예제 4
# dict_variable = {
#     "이름": "정우영", 
#     "생년월일" : "19000101", 
#     "회사" : "하이퍼그로스", 
# }

# for key in dict_variable:
#     print(key, dict_variable[key])

# # 예측: 이름 정우영 / 생년월일 19000101 / 회사 하이퍼그로스

# 예제 5
# dict_variable = {
#     "이름": "정우영", 
#     "생년월일" : "19000101", 
#     "회사" : "하이퍼그로스", 
# }

# for key, value in dict_variable.items():
#     print(key, value)

# # 예측: 이름 정우영 / 생년월일 19000101 / 회사 하이퍼그로스

# 예제 6
# dict_variable = {
#     "이름": "정우영", 
#     "생년월일" : "19000101", 
#     "회사" : "하이퍼그로스", 
# }

# print("나이" in dict_variable) # False

# 예제 7
# dict_variable = {
#     "이름": "정우영", 
#     "생년월일" : "19000101", 
#     "회사" : "하이퍼그로스", 
# }

# if "거주지" not in dict_variable:
#     dict_variable["거주지"] = "서울특별시"
#     # dict_variable의 키값 중에 거주지가 없으면 거주지:서울특별시 키,밸류 추가

# print(dict_variable)
# # 이름 정우영 / 생년월일 19000101 / 회사 하이퍼그로스 / 거주지 서울특별시

# 예제 8
# list_variable = []

# try:
#     list_variable.append(0)
#     list_variable.append(1)
#     list_variable.append(2)
#     print(list_variable[3])

# except:
#     print("에러가 발생했습니다.")
#     print("에러의 원인은 무엇인가요?")
# # 예측: 에러가 발생했습니다. / 에러의 원인은 무엇인가요?
# # ->list_variable은 0~2의 list를 가지는데 3의 리스트값을 출력하라고 해서 오류가 나게됨

# 예제 9
# try:
#     number = 1
#     if number == 1:
#         print(number)
# except:
#     print("에러가 발생했습니다.")
#     print("에러의 원인은 무엇인가요?")
# # try구문이 실행되므로 1이 출력된다

# 예제 10
# n = 10
# total = 0
# for number in range(0, n+1):
#     if number % 2 == 0:
#         total += number * 2
#     elif number % 2 == 1:
#         total += number + 1 * 3
# print(total) # 0 4 4 6 8 8 12 10 16 12 20 -> 60 + 40 = 100