def getGrade(x):
    if (x > 90):
        return 'A'
    elif (x > 80):
        return 'B'
    elif (x > 70):
        return 'C'
    elif (x > 60):
        return 'D'
    else:
        return 'F'


score = int(input("점수를 입력하시요"))

print(getGrade(score))