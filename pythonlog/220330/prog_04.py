UinputNumber = int(input("정수를 입력하십시오 :")) # 정수 입력
print("약수 : ", end="") # 출력해줌과 동시에 개행문자 제거
for i in range(1, UinputNumber + 1): # 1부터 사용자가 입력한 값 +1까지
    if(UinputNumber % i == 0): # 사용자의 입력과 i를 나눴을때 나머지가 0인 약수인 경우
        print(i, end=" ") # 약수출력과 동시에 개행문자 제거