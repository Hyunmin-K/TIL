# 문제 1
# num = int(input("정수를 입력하세요 > "))
# if num <0:
#     num = num * (-1)
# print(num)

# 문제 2
# number_list = []
# cnt = 0
# for number in number_list:
#     cnt = cnt + 1
# print(cnt)

# 문제 3
# number_list = [-1, -2, -3, -4, -5]
# sum = 0
# for number in number_list:
#     sum += number
# print(sum)

# 문제 4
# number_list = [2, 3, 5, 7]
# cnt, sum = 0, 0
# for number in number_list:
#     cnt = cnt + 1
#     sum = sum + number
# answer = sum / cnt
# print(answer)

# 문제 5
# number_list = [-1, -2, 3]
# multiply = 1
# for number in number_list:
#     multiply = multiply * number
# print(multiply)

# 문제 6
# number_list = [1, 1, 1]
# max_num = number_list[0]
# for number in number_list:
#     if max_num < number:
#         max_num = number
# print(max_num)

# # 문제 7
number_list = [5, 5, 5, 2]
min_num = number_list[0]
for number in number_list:
    if min_num > number:
        min_num = number
print(min_num)