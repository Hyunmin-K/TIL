#2576 홀수
sum = 0
min_n = 100
for i in range(7):
    n = int(input())
    if n % 2 == 1 :
        sum+=n
        if min_n > n:
            min_n = n
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min_n)