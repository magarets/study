import sys

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def radi(a, b):
    return a*b
def Na(a, b):
    return a/b


x = int(input("첫 번재 정수를 입력하시오"))
y = int(input("두 번재 정수를 입력하시오"))

print(f"{x} + {y} = ", add(x, y))
print(f"{x} - {y} = ", sub(x, y))
print(f"{x} * {y} = ", radi(x, y))
print(f"{x} / {y} = ", Na(x, y))

