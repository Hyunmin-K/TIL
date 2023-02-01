#블랙잭

n,m = map(int,input().split())
max_blk = 0
number = list(map(int,input().split()))
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans = number[i]+number[j]+number[k]
            if ans <= m and ans > max_blk:
                max_blk = ans
print(max_blk)