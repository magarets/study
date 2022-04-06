x = float(input("pH를 입력하시오: "))

if(x == 7): # 농도가 7일때
    print("중성 입니다.")
elif(x <= 6): #농도가 6일때
    print("산 입니다.")
elif(x >= 8): #농도가 8일때
    print("알칼리 입니다.")