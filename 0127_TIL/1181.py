#단어 정렬
T = int(input())
s_list=[]
for i in range(T):
    s = input()
    if s not in s_list:
        s_list.append(s)
sort_list = sorted(s_list,key=ascii,reverse=False)
sort_list = sorted(sort_list,key=len,reverse=False)

for i in range(len(sort_list)):
    print(sort_list[i])