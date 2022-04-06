import random

CRandNumber = random.randint(1, 3)

def WinnerIsCpu(): # 컴퓨터가 이겼을 경우를 출력
    print("컴퓨터가 이겼음")
def WinnerIsUser(): # 사용자가 이겼을 경우를 출력
    print("사용자가 이겼음")

URandNumber = int(input("선택하시오(1: 가위 2: 바위 3: 보"))
if(URandNumber == CRandNumber): #비기는경우를 최상위 if문으로 배치하여 로직 최소화
    print("비겼음")
elif(URanNumber == 1): #사용자가 가위일때
    if(CRandNumber == 2): #사용자가 가위, 컴퓨터가 바위
        WinnerIsCPU()
    elif(CRandNumber == 3): #사용자가 가위, 컴퓨터가 보
        WinnerIsUser()

elif(URanNumber == 2): #사용자가 바위일때
    if(CRandNumber == 1): #사용자가 바위, 컴퓨터가 가위
        WinnerIsUser()
    elif(CRandNumber == 3): #사용자가 바위, 컴퓨터가 보
        WinnerIsCpu()

elif(URanNumber == 3): #사용자가 보일때
    if(CRandNumber == 1): #사용자가 보, 컴퓨터가 가위
        WinnerIsCPU()
    elif(CRandNumber == 2): #사용자가 보, 컴퓨터가 바위
        WinnerIsUser()