T = int(input())
test = [0,1,2,3,4,5,6,7,8,9]
for j in range(T):
    answer = []
    m = int(input())
    for i in range(1,100):
        answer = test
        n = m*i
        while(n>0):
            mod = n%10
            n = n//10
            if mod in test:
                answer.remove(mod)
        if answer == []:
            print(f'#{j+1} {m*i}')
            test = [0,1,2,3,4,5,6,7,8,9]
            break