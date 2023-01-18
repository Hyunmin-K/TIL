#9498 시험성적
# a = int(input())
# if 90<= a <=100:
#     print("A")
# elif 80 <= a < 90:
#     print("B")
# elif 70 <= a < 80:
#     print("C")
# elif 60 <= a < 70:
#     print("D")
# else:
#     print("F")

#9093 단어 뒤집기
# T = int(input())
# for i in range(T):
#     s = list(map(str,input().split()))
#     for j in range(len(s)):
#         for k in range(len(s[j])-1,-1,-1):
#             print(s[j][k],end='')
#         print(end=' ')
#     print()

#11721 열 개씩 끊어 출력하기
# line = input()
# for i in range(len(line)):
#     print(line[i],end='')
#     if i%10 == 9:
#         print()

#2947 나무 조각
answer = [1,2,3,4,5]
num_list = list(map(int,input().split()))
while True:
    for i in range(4):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            for j in range(5):
                print(num_list[j],end=' ')
            print()
    if num_list == answer:
        break
