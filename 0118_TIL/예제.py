# 2789 유학 금지
# compare = 'CAMBRIDGE'
# line = input()
# for i in line:
#     if i in compare:
#         continue
#     else:
#         print(i,end='')

#2675 문자열 반복
# T = int(input())
# for i in range(T):
#     r, s = map(str, input().split())
#     for j in range(len(s)):
#         print(s[j]*int(r),end='')
#     print()

#10988 팰린드롬인지 확인하기
# s = input()
# line1 = []
# line2 = []
# for i in range(len(s)):
#     line1.append(s[i])
#     line2.append(s[-i-1])
# if line1 == line2:
#     print(1)
# else:
#     print(0)

#17249 태보태보 총난타
# taebo = input()
# left, right = 0,0
# left_cnt, right_cnt = 0,0
# for i in range(len(taebo)):
#     if taebo[i:i+5] == '(^0^)':
#         left = i
#         right = i+5

# for i in range(left):
#     if taebo[i] == '@':
#         left_cnt +=1
# for i in range(right,len(taebo)):
#     if taebo[i] == '@':
#         right_cnt +=1
# print(left_cnt, right_cnt)

#2941 크로아티아 알파벳
#10809 알파벳 찾기