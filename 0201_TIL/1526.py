#가장 큰 금민수

n = input()
chk = [4,7]
max_gold = 0
for i in range(1,int(n)+1):
    num = i
    while num !=0:
        if num%10 in chk:
            num = num //10
        else:
            break
    if num ==0:
        if max_gold < i:
            max_gold = i
print(max_gold)