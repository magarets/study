for i in range(2, 10): # n단을 정함
    print(f"# {i}단")
    for j in range(1, 10): # n단에서 나올 수 있는 곱들을 출력
        print(i * j, end=" ") # n * 1 ~ 9
    print("")