import random

def AddNumber(x, y): #x에는 첫번째 랜덤값, y에는 두번째 랜덤값이 들어감.
    UInputNum = int(input(f"{x} + {y}의 값은? ")) # UInputNum 은 사용자의 입력임
    if(x + y == UInputNum):
        print("맞았습니다")
    else:
        print("틀렸습니다")

def SubNumber(x, y):
    UInputNum = int(input(f"{x} - {y}의 값은? "))
    if (x - y == UInputNum):
        print("맞았습니다")
    else:
        print("틀렸습니다")

def MultNumber(x, y):
    UInputNum = int(input(f"{x} * {y}의 값은? "))
    if (x * y == UInputNum):
        print("맞았습니다")
    else:
        print("틀렸습니다")

def DivNumber(x, y):
    UInputNum = float(input(f"{x} / {y}의 값은? "))
    if (x / y == UInputNum):
        print("맞았습니다")
    else:
        print("틀렸습니다")

RNum_First = random.randint(1, 10) # 첫번째 피연산자의 값을 1 ~ 10사이의 정수중, 하나의 수를 임의로 생성
RNum_Second = random.randint(1, 10) #첫번째 피연산자의 값을 1 ~ 10사이의 정수중, 하나의 수를 임의로 생성


RCalculatorNumber = random.randint(1, 4) # 1 : 덧셈, 2 : 뺄셈, 3 : 곱셈, 4 : 나눗셈
if(RCalculatorNumber == 1): #덧셈이 나왔을 경우
    AddNumber(RNum_First, RNum_Second)
if(RCalculatorNumber == 2): #뺄셈이 나왔을 경우
    SubNumber(RNum_First, RNum_Second)
if (RCalculatorNumber == 3): # 곱셈이 나왔을 경우
    MultNumber(RNum_First, RNum_Second)
if(RCalculatorNumber == 4): # 나눗셈이 나왔을 경우
    DivNumber(RNum_First, RNum_Second)
