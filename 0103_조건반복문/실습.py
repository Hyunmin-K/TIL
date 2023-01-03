# num = int(input("정수를 입력하세요 > "))
# if num > 0:
#     print(True)
# else:
#     print(False)

# num1 = int(input("첫 번째 정수를 입력하세요 > "))
# num2 = int(input("두 번째 정수를 입력하세요 > "))
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# else:
#     print(False)

# num = int(input("정수를 입력하세요 > "))
# if 1 < num < 10:
#     print(True)
# else:
#     print(False)

# num = int(input("정수를 입력하세요 > "))
# if num > 0 and num%2 == 0:
#     print(True)
# else:
#     print(False)

# num = int(input("정수를 입력하세요 > "))
# if num > 100 or num < 0:
#     print("에러")
# elif num >=60:
#     print("합격")
# else:
#     print("불합격")

# word = input("문자열을 입력하세요 > ")
# for i, key in enumerate(word):
#     print(word[-i-1])

# num1 = int(input("첫 번째 정수를 입력하세요 > "))
# num2 = int(input("두 번째 정수를 입력하세요 > "))
# if num1 > num2 :
#     for i in range(num2+1,num1):
#         print(i)
# elif num1 < num2 :
#     for i in range(num1+1, num2):
#         print(i)
# else :
#     print(False)

# num1 = int(input("첫 번째 정수를 입력하세요 > "))
# num2 = int(input("두 번째 정수를 입력하세요 > "))
# if num1 > num2 :
#     for i in range(num1-1, num2,-1):
#         print(i)
# elif num1 < num2 :
#     for i in range(num2-1, num1, -1):
#         print(i)
# else :
#     print(False)

# num = int(input("정수를 입력하세요 > "))
# if num < 1:
#     print(False)
# else:
#     for odd in range(num):
#         if odd % 2 == 1:
#             print(odd)

for i in range(2,10):
    for j in range(2,10):
        print(f"{i} X {j} = {i*j}")
        