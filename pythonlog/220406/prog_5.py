def checkpass(passwd): # 패스워드를 총 3단계에 걸쳐서 검사.
    if(len(passwd) < 8): # 1. 패스워드의 길이가 8개 이상이 아닐 때
        return False # 패스워드 검증실패시 0 리턴
    else:
        if(passwd.isupper() or passwd.islower()): # 2. 패스워드중 대,소문자가 최소 1개이상일 때.패스워드 전체가 대문자이거나, 소문자이면 리턴
            return False # 패스워드 검증 실패
        else:
            if(any(map(str.isdigit, passwd))): # 3. 패스워드에 적어도 한개이상의 숫자가 포함되있을 때.
                                               # 3-1 str.isdigit 함수는 문자열에서 모든문자가 숫자일경우 True
                                               # 3-2 map 함수는 왼쪽인자함수를 리스트의 각각의 객체에 적용시켜서 적용시킨값을 반환합니다. 즉, passwd 에서 문자를 하나씩 떼서 str.isdigit() 함수를 실행시킨 결과를 반환하는것입니다.
                                               # any() 는 () 안에 있는 함수들의 실행결과값중, 하나이상이(단 한개라도) 참일경우 참을 반환합니다.any(map(str.isdigit, str)) => 문자열에 숫자가 최소 하나이상 포함되어있을경우 TRUE를 반환
                return True # 패스워드 검증성공

flag = False # boolen 변수 선언
while(not flag): # 사용자값이 올바른 패스워드일때까지 반복
    passwd = input("패스워드를 입력하시오: ") # 사용자로부터 passwd 값 입력
    flag = checkpass(passwd) # flag boolen 변수에 checkpass(패스워드 검증 결과 T/F) 함수 리턴값 저장
    if(not flag): # 값이 틀렸을때만 경고문 출력
        print("사용할 수 없습니다! 다시 입력하세요") # 패스워드 인증실패시 출력
print(f"{passwd} 는 사용할 수 있습니다.") # 성공하면 while 문 탈출 -> 성공문 출력