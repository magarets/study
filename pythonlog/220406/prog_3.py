def calc(a, b): # 사칙연산 계산수행함수
    return a+b, a-b, a*b, a/b # 덧셈, 뺄셈, 곱셈, 나눗셈값을 한번에 리턴해준다

x = int(input("첫 번째 정수를 입력하세요 : ")) # x = 첫번째 입력값
y = int(input("두 번째 정수를 입력하세요 : ")) # y = 두번째 입력값

print(f"{calc(x, y)}이 리턴되었습니다") # 사칙연산 함수호출
