def geintRange():
    flag = 0
    while (flag != 1):
        flag = 0
        x = int(input("월을 입력하시오(1부터 12사이의 값)"))
        if (x >= 1 and x <= 12):
            flag = 1
    flag = 0
    while (flag != 1):
        flag = 0
        y = int(input("일을 입력하시오(1부터 31사이의 값)"))
        if (y >= 1 and y <= 31):
            flag = 1
    print(f"입력하신 날짜는 {x}월 {y}일 입니다")

print("날짜를 입력하시오")
geintRange()






