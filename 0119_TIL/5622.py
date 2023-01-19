# s = input()
# time = 0
# for i in range(len(s)):
#     if s[i] in 'ABC':
#         time +=3
#     elif s[i] in 'DEF':
#         time +=4
#     elif s[i] in 'GHI':
#         time +=5
#     elif s[i] in 'JKL':
#         time +=6
#     elif s[i] in 'MNO':
#         time +=7
#     elif s[i] in 'PQRS':
#         time +=8
#     elif s[i] in 'TUV':
#         time +=9
#     elif s[i] in 'WXYZ':
#         time +=10
# print(time)

s = input()
time = 0
answer = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in s:
    for j in range(len(answer)):
        if i in answer[j]: 
            time = time + j+3
print(time)