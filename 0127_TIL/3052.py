#나머지
rest_list = []
for i in range(10):
    n = int(input())
    rest = n%42 
    if rest not in rest_list:
        rest_list.append(n%42)
print(len(rest_list))