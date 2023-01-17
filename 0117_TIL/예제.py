# 10818 최소, 최대
# n = int(input())
# num_list = list(map(int,input().split()))
# num_max = num_list[0]
# num_min = num_list[0]
# for i in range(n):
#     if num_max < num_list[i]:
#         num_max = num_list[i]
#     if num_min > num_list[i]:
#         num_min = num_list[i]

# print(num_min, num_max)

# 11720 숫자의 합

# n = int(input())
# number = input()
# sum = 0
# for i in range(n):
#     sum += int(number[i])
# print(sum)

# 2750 수 정렬하기

# n = int(input())
# num_list = []
# for i in range(n):
#     m = int(input())
#     num_list.append(m)
# sort_list = sorted(num_list)
# for i in range(len(sort_list)):
#     print(sort_list[i])

# 2562 최댓값
num_list = []
max = 0
max_index = 0
for i in range(9):
    n = int(input())
    num_list.append(n)
    if max < num_list[i]:
        max = num_list[i]
        max_index = i+1
print(max)
print(max_index)