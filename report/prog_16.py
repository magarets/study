Board_SIZE = int(input("게임판의 크기: ")) # 게임판의 크기를 정수형으로 입력받음.

print("") # 입력받고 개행문자 출력
for i in range(Board_SIZE): # 알고리즘상, 맨 첫번째 오는 줄(지붕->가로줄)은 입력받은 게임판의 크기만큼 무조건 출력
    print(" ---", end = "") # end = ""를 넣음으로써, 출력하고 개행이 이루어지지않도록 함.
print("")# 개행문자
for l in range(Board_SIZE): # 이후로 오는 게임판은 (세로 줄 : 게임판의 크기 +1, 가로 줄 : 게임판의 크기) 에 비례하게 증가함.
    for i in range(Board_SIZE + 1): # 게임판의 세로줄을 출력하는 반복문
        print("|   ", end = "") # 세로줄 출력
    print("") # 한 줄을 출력 후, 개행

    for i in range(Board_SIZE): # 게임판의 가로줄을 출력하는 반복문
        print(" ---", end = "") # 가로줄 출력
    print("") # 한 줄을 출력 후, 개행