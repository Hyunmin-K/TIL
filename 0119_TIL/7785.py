#회사에 있는 사람
n = int(input())
name_dict = {}
for i in range(n):
    a,b = map(str,input().split())
    if b == 'enter':
        name_dict[a] = 'name'
    else:
        del name_dict[a]

for i in sorted(name_dict.keys(),reverse=True):
    print(i)