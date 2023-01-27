#대칭 차집합

n = list(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))
dict_c = {}
cnt = 0
c = a+b
for i in c:
    if i in dict_c:
        dict_c[i] +=1
        cnt -=1
    else:
        dict_c[i] = 1
        cnt +=1
print(cnt)