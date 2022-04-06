def testPrime(n):
    flag = 0
    for i in range(1, n):
        if(n % i == 0):
            flag+=1
    if(flag>1):
        return 0

for i in range(1, 101):
    if(testPrime(i) != 0):
        print(i, end=" ")