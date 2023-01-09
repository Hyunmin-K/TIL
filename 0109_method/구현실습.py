#문제1
# line = input("문자열을 입력하세요 > ")
# cnt = 0
# answer = -1
# for find in line:
#     if find == 'e':
#         answer = cnt
#     cnt = cnt+1
# print(answer)

#문제2
# line = list(map(str,input("문자열을 입력하세요 > ").split()))
# answer = {}
# for split_line in line:
#     if split_line in answer:
#         answer[split_line] +=1
#     else:
#         answer[split_line] = 1
# for key, value in answer.items():
#     print(key, value)

#문제3
# line = input("문자열을 입력하세요 > ")
# answer = ''
# for find in line:
#     if find == 'e':
#         find = ''
#     answer = answer+find
# print(answer)

#문제4
# line1,line2 = map(str,input("문자열을 입력하세요 > ").split())
# answer = 0
# for i in line1:
#     if i == line2:
#         answer = answer+1
# print(answer)

#문제5
# line1,line2, line3 = map(str,input("문자열을 입력하세요 > ").split())
# print(line1, line2, line3, sep='-')

#문제6
line = int(input("문자열을 입력하세요 > "))
sum = 0
if line >= 0:
    while(True):
        sum = sum + (line%10)
        line = line // 10
        if line <=0:
            break
else:
    sum = -1
print(sum)