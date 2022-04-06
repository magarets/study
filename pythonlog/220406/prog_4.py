def getGrade(x): # x = 파라미터(점수) 성적에따른 학점부여 함수
    if (x >= 90): # x>=90
        return 'A'
    elif (x >= 80): # 90> x >=80
        return 'B'
    elif (x >= 70): # 80> x >=70
        return 'C'
    elif (x >= 60): # 70> x >=60
        return 'D'
    else: #60> x
        return 'F'


score = int(input("점수를 입력하시오")) # score : 사용자 입력 값(점수)

print(getGrade(score)) # 학점계산함수호출