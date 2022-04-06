def calc(a, b):
    return a+b, a-b, a*b, a/b

x = int(input("첫 번째 정수를 입력하세요 : "))
y = int(input("두 번째 정수를 입력하세요 : "))

print(f"{calc(x, y)}이 리턴되었습니다")
