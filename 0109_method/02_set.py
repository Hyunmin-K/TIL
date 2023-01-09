my_list = ['서울', '서울', '대전', '광주',
'서울', '대전', '부산', '부산']
one_list = []
for one in my_list:
    if one not in one_list:
        one_list.append(one)
print(one_list)

print(set(my_list))