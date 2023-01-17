T = int(input())
list_31 = [1,3,5,7,8,10,12]
list_30 = [4,6,9,11]
for i in range(T):
    day = input()
    year = day[0:4]
    month = day[4:6]
    date = day[6:8]
    if 0 <= int(year) <= 9999:
        if 1 <= int(month) <= 12:
            if int(month) in list_31:
                if 1 <= int(date) <=31:
                    print(f'#{i+1} {year}/{month}/{date}')
            elif int(month) in list_30:
                if 1 <= int(date) <= 30:
                    print(f'#{i+1} {year}/{month}/{date}')
            elif int(month) == 2:
                if 1 <= int(date) <= 28:
                    print(f'#{i+1} {year}/{month}/{date}')
                else:
                    print(f'#{i+1} -1')
            else:
                print(f'#{i+1} -1')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')