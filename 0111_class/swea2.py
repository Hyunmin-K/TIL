#2047 신문 헤드라인
# line = input()
# print(line.upper())

#2025 N줄덧셈
# num = int(input())
# result = 0
# for i in range(1,num+1):
#     result +=i
# print(result)

#1936 1대1 가위바위보
# a, b = map(int, input().split())
# if a == 1 and b == 3:
#     print('A')
# else:
#     if a<b:
#         print('B')
#     else:
#         print('A')

#2027 대각선 출력하기
# line = ''
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             line+='#'
#         else:
#             line+='+'
#         if (len(line))%5 ==0:
#             print(line)
#             line = ''

#2058 자릿수 더하기
# num = int(input())
# result = 0
# while(True):
#     mod = num%10
#     result +=mod
#     num = num//10
#     if num <=0:
#         break
# print(result)

#2019 더블더블
num = int(input())
result = 1
for i in range(0,num+1):
    print(result,end=' ')
    result *=2