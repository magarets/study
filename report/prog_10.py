result = 0 # 누적변수 result 를 선언함. 누적변수이기에 초기값을 0으로 설정하였음.

UinputNum = int(input("n의 값을 입력하시오 :")) # UinputNum 에 사용자의 입력값 추가
for i in range(1, UinputNum + 1): # 1부터 사용자가 입력한 값까지 반복
    result += i*i # result에 i^i를 누적
print(f"계산값은 {result} 입니다.")