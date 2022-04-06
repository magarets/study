UinputNum = int(input("정수를 입력하십시오 : "))

for i in range(1, UinputNum+1): # 1 ~ 사용자가 입력한 값 +1 까지 열의 갯수를 정함
    for j in range(i): # 1 ~ i까지 행의 갯수를 정함
        print(j+1, end = " ") # 나온값에 +1을 하여 식 완성
    print("")