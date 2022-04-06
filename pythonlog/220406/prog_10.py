def testPrime(n): # 매개변수 n = i
    flag = 0 # 해당수가 소수인지 판별하기위한 약수의 갯수 저장변수
    for i in range(1, n): #1부터 n-1까지 전부나눔
        if(n % i == 0): # 전부 나눠서 나머지가 0인경우 (약수인경우)
            flag+=1 # 약수 카운터변수 1증가
    if(flag>1): # 만약에 약수의 갯수가 2개이상일 때(여기서는 자기자신을 포함안했으므로 소수면 flag 값은 1이나와야 정상.
        return 0

for i in range(1, 101): # 1부터 100까지의 수 i
    if(testPrime(i) != 0): # 소수를 찾는 testPrime에 1부터 100까지 인자로 넣으면서 호출하면서 testPrime에서 소수가 아닐때 리턴한 0 값이 아닐경우 (즉, 소수일경우)
        print(i, end=" ") # 소수를 출력