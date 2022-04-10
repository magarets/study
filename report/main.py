import random

CRandNum = random.randint(1, 100)

UNumber = -1 # while에 진입하기위한 사용자입력값 초기화. 대신 1 ~ 100사이의 정수가 아니어야 함
while(UNumber != CRandNum):
    UNumber = int(input("1부터 100사이의 숫자를 맞추시오 :"))
    if(UNumber < CRandNum):
        print(" up! ")
    elif(UNumber > CRandNum):
        print(" down! ")
print("congrat!")