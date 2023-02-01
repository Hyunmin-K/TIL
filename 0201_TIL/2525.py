# 오븐 시계
h, m = map(int, input().split())
cook = int(input())

a_h, a_m = h, m+cook
while a_m >= 60:
    if a_m >= 60:
        a_h = a_h + 1
        a_m = a_m - 60
    if a_h >= 24:
        a_h = a_h - 24
print(a_h, a_m)