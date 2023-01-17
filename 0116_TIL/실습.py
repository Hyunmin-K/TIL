# 10039 평균 점수
# sum = 0
# for i in range(5):
#     num = int(input())
#     if num <40:
#         num = 40
#     sum = sum+num
# avg = sum/5
# print(int(avg))

# 10871 X보다 작은 수
# T, std= map(int,input().split())
# A = list(map(int, input().split()))
# for i in range(T):
#     if A[i] < std:
#         print(A[i],end=' ')

# 2480 주사위 세개
# d1, d2, d3= map(int, input().split())
# answer = 0
# if d1 == d2 == d3:
#     answer = 10000 + d1*1000
# elif d1 == d2 or d1 == d3:
#     answer = d1 * 100 + 1000
# elif d2 == d3:
#     answer = d2 * 100 + 1000
# else:
#     answer = max(d1, d2, d3) * 100
# print(answer)

#10886 not cute/cute
# count_0 = 0
# count_1 = 0
# T = int(input())
# for i in range(T):
#     cute = int(input())
#     if cute == 0:
#         count_0 +=1
#     else:
#         count_1 +=1
# if count_0 < count_1:
#     print("Junhee is cute!")
# else:
#     print("Junhee is not cute!")

#2506 점수계산
T= int(input())
sum = 0
A = list(map(int, input().split()))
for i in range(T):
    if A[i] == 1:
        sum +=1
        for j in range(i+1,T):
            if A[j] ==1:
                sum += 1
            else:
                break
print(sum)