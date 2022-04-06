import sys

def add(a, b): # 덧셈함수
    return a+b
def sub(a, b): # 뺄셈함수
    return a-b
def radi(a, b): # 곱셈함수
    return a*b
def Na(a, b): #나눗셈함수
    return a/b


x = int(input("첫 번재 정수를 입력하시오")) # x = 첫번째 입력값
y = int(input("두 번재 정수를 입력하시오")) # y = 두번째 입력값

## 계산결과 출력 ##
print(f"{x} + {y} = ", add(x, y))
print(f"{x} - {y} = ", sub(x, y))
print(f"{x} * {y} = ", radi(x, y))
print(f"{x} / {y} = ", Na(x, y))
################

