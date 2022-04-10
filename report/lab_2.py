count = 1 # 소수인지 판별하는 값 초기화
count_limit = 0 # 갯수를 찾는 값 초기화
while count_limit < 50: # 소수가 50개일때 종료
    count += 1 # 피벗이 되는 값 증가
    count_flag = 0 # 해당수의 약수의 갯수
    for i in range(1, count+1): # 해당숫자의 약수의 갯수를 구하는 반복문
        if(count % i == 0): # i가 count의 약수일 경우 count_flag 증가
            count_flag += 1
    if(count_flag > 2): # 피벗숫자의 약수가 3개 이상일 경우. 즉, 소수가 아닐경우
        continue # while 문으로 돌아감
    count_limit += 1 # 먖댜면 소수의 갯수를 증가시키고 출력
    print(count, end=" ")