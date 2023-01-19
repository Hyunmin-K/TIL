#학점계산
s = input()
num = 0.0
if 'A' in s:
    num += 4.0
elif 'B' in s:
    num += 3.0
elif 'C' in s:
    num += 2.0
elif 'D' in s:
    num += 1.0
if '+' in s:
    num +=0.3
elif '-' in s:
    num -=0.3
print(num)