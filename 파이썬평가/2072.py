T = int(input())
for i in range(T):
    sum = 0
    num_list = list(map(int,input().split()))
    for j in range(10):
        if num_list[j] %2 == 1:
            sum +=num_list[j]
    print(f'#{i+1} {sum}')
    