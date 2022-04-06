def PrintNumber(Number): #작은값을 함수로 넘겨서 출력
    print(f"제일 작은 정수는 {Number} 입니다.")

x, y ,z = eval(input("3개의 정수를 입력하시오 : "))

if(x > y):
    if(y > z): # x, y를 비교해서 y가 작을때 => y랑 z를 비교해서 z가 작을경우
        PrintNumber(z)
    else: # y랑 z를 비교해서 y가 작을경우
        PrintNumber(y)
elif(x < y):
    if(x < z): #x, y를 비교해서 x가 작을때 => z랑 x를 비교해서 x가 작을경우
        PrintNumber(x)
    else: #x 랑 z를 비교해서 z가 작을경우
        PrintNumber(z)