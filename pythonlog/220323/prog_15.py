x = int(input("정수를 입력하시오: "))

if(x % 3 == 0 and x % 5 == 0): # x가 3의 배수이면서 5의배수일때
    print("Python Express")
elif(x % 3 == 0 and x % 5 != 0): # x가 3의 배수이지만 5의배수는 아닐때
    print("Python")
elif(x % 3 != 0 and x % 5 == 0): # x가 3의 배수는 아니지만 5의배수일때
    print("Express")
else:
    print("Nop")