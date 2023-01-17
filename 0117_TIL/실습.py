# 9085 더하기
# T = int(input())
# for i in range(T):
#     sum = 0
#     n = int(input())
#     num_list = list(map(int,input().split()))
#     for j in range(n):
#         sum +=num_list[j]
#     print(sum)

# 10824 네 수
# num_list = list(map(str,input().split()))
# n1 = num_list[0]+num_list[1]
# n2 = num_list[2]+num_list[3]
# answer = int(n1)+int(n2)
# print(answer)

# 3009 네 번째 점
# a = [0 for i in range(3)]
# b = [0 for i in range(3)]
# for i in range(3):
#     a[i], b[i] = map(int,input().split())

# for i in range(3):
#     if a.count(a[i]) == 1:
#         answer_x = a[i]
#     if b.count(b[i]) == 1:
#         answer_y = b[i]
# print(answer_x, answer_y)

# 10952 A+B -5
# while True:
#     a, b = map(int, input().split())
#     if a==0 and b==0:
#         break
#     print(a+b)

#1110 더하기 사이클
n = int(input())
n1, n2, cnt = 0, 0, 0
ans1, ans2 = 0,0
n1 = n // 10
n2 = n % 10
n3 = (n1 + n2) % 10
while True:
    cnt+=1    
    if n2*10 + n3 != n:
        n1, n2 = n2, n3
        n3 = (n1 + n2) % 10
    else:
        break
print(cnt)