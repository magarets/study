def SumNumbers(a, b): # 매개변수 a = x, b = y / 사용자로부터 입력받은 x, y를 더하는 함수
    print(f"두 정수 {a}, {b}의 합은?")

x = int(input("첫 번재 정수를 입력하시오"))  # 첫 번째 사용자 입력값
y = int(input("두 번째 정수를 입력하시오"))  # 두 번째 사용자 입력값
SumNumbers(x, y)