#숫자의 개수
A = int(input())
B = int(input())
C = int(input())
answer = A*B*C
answer = str(answer)
for i in range(10):
    cnt = 0
    for j in range(len(answer)):
        if answer[j] == str(i):
            cnt +=1
    print(cnt)