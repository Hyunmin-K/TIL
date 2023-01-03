# num = int(input("숫자를 입력하세요 > "))
# if num % 2 == 0:
#     print("짝수입니다")
# if num % 2 == 1:
#     print("홀수입니다")

dust = 170
if dust >150:
    print("매우나쁨")
    if dust > 300:
        print("실외 활동을 자제하세요.")
elif dust >80:
    print("나쁨")
elif dust > 30:
    print("보통")
else:
    if dust >=0:
        print("좋음")
    else:
        print("값이 잘못되었습니다.")

