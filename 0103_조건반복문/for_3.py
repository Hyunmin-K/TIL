word = 'banana' # a가 있으면 1을 출력
for check in word:
    if check == 'a':
        print(1)
print('=====')

for char in word:
    if char == 'a':
        continue
    print(char)
