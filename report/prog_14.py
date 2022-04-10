for isPrimeNumber in range(2, 21): # isPrimeNumber 에는 구하려는 숫자범위인 2부터 20까지의 수가 차례로 들어감
    flag = 0 # 차례로 들어온 isPrimeNumber의 약수의 갯수를 저장하는 변수
    for CheckPrimeNum in range(1, isPrimeNumber): # isPrimeNumber가 소수인지 판별하기위해서 1에서 isPrimeNumber-1 (자기자신 제외)까지의 숫자를 모두 나눠본다.
        if(isPrimeNumber % CheckPrimeNum == 0): # 만약 나눠지면 해당수는 약수란 뜻임
            flag += 1 # 약수의 갯수 1 증가
    if(flag <= 1): # flag는  isPrimeNumber에 대한 약수의 갯수임. 즉, 약수의 갯수가 2개 이하일 때(소수일때)
        print(isPrimeNumber, end=" ") # 해당수를 출력함