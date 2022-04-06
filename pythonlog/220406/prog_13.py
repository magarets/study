import random

def dice_game(): # dice game 호출
    print("===== dice_game() 호출 =====")
    UDiceNum = random.randint(1, 6) # 사용자의 주사위 값 변수인 UdiceNum에 주사위 값을 랜덤으로 부여
    print(f"사용자: 주사위= {UDiceNum}")
    CrandDice = random.randint(1, 6) # 컴퓨터 주사위 값 변수인 CrandDice에 랜덤으로 주어지는 주사위 값 변수
    print(f"컴퓨터: 주사위= {CrandDice}")

    if(UDiceNum == CrandDice): # 사용자의 값이랑 컴퓨터의 값이 같을 때
        print("무승부")
    elif(UDiceNum > CrandDice): # 사용자의 값이 컴퓨터의 값보다 클 때
        print("인간승리")
    else: # 사용자의 값이 컴퓨터의 값보다 작을 때
        print("컴퓨터승리")

flag = 'N' # 중단여부를 확인하는 flag변수 초기화
while(flag == 'N' or flag == 'n'): # 중단할지 여부를 확인. N, n (대소문자구별)이외의 값이 들어가면 종료
    dice_game() # dice_game 호출
    print("===== dice_game() 복귀 =====")
    flag = input("중단할까요? Y/N")

