# #문제 2029 
# number = int(input())
# for i in range(number):
#     a,b = map(int,input().split())
#     print(f'#{i+1} {a//b} {a%b}')

# #문제 2071
# number = int(input())
# for i in range(number):
#     a = list(map(int,input().split()))
#     print(f'#{i+1} {round(sum(a)/10)}')

#문제 1938
# a,b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

#문제 2046
# a = int(input())
# line = ''
# for i in range(a):
#     line = line + '#'
# print(line)

#문제 2068
number = int(input())
max = 0
for i in range(number):
    a = list(map(int,input().split()))
    max = a[0]
    for j in range(len(a)):
        if a[j] >= max:
            max = a[j]
    print(f'#{i+1} {max}')
