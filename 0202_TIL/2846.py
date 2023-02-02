#오르막길

n = int(input())
n_list = list(map(int,input().split()))
asc = []
max_asc = 0
for i in range(n-1):
    asc.append(n_list[i+1] - n_list[i])
for i in range(len(asc)):
    sum = 0
    if asc[i] >0:
        sum+=asc[i]
        for j in range(i+1,len(asc)):
            if asc[j]>0:
                sum+=asc[j]
            else:
                break
        if max_asc < sum:
            max_asc = sum
print(max_asc)