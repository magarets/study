def randsum(a, b):
    Uinput = int(input(f"두 정수 {a}, {b}의 합은?"))
    if(a + b == Uinput):
        return 1
    else:
        return 0
x = int(input("첫 번재 정수를 입력하시오"))
y = int(input("두 번째 정수를 입력하시오"))
if(randsum(x, y)):
    print("맞았습니다!")
else:
    print("틀렸습니다....ㅠㅠ")