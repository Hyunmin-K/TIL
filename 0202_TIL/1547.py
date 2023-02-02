#공

n = int(input())
cup = 1
error = -1
for i in range(n):
    x,y = map(int,input().split())
    if x and y not in [1,2,3]:
        print(cup = error)
        break
    if x == cup:
        cup = y
    elif y == cup:
        cup = x
print(cup)