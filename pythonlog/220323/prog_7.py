Stature = int(input("키를 입력하시오(cm): "))
Age = int(input("나이를 입력하시오: "))

if(Stature >= 140 and Age >= 10): #키가 140 이상이면서, 나이가 10살 이상일경우
    print("타도 좋습니다")
else: #키가 140이상이면서, 나이가 10살이상이 아닌경우
    print("죄송합니다")