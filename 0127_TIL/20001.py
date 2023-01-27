#고무오리 디버깅

input()
stack = []
while True:
    s = input()
    if s == '고무오리 디버깅 끝':
        break
    elif s == '문제':
        stack.append(s)
    elif s == '고무오리':
        if stack == []:
            stack.append('문제')
            stack.append('문제')
        else:
            stack.pop()
if stack == []:
    print('고무오리야 사랑해')
else:
    print('힝구')        
