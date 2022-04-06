def deci2bin(num, lists):
    s = num // 2 # 피벗값 (초기엔 num)을 s에 2씩 나눠주면서 자리수를 늘려감.
    r = num % 2 # 자리수에 들어갈 숫자 0, 1을 구하는 변수
    lists.append(r) # lists 끝에 한글자씩 붙여서 왼쪽부터 오른쪽으로 2진수 완성

    if(s == 0): # 만약 피벗값이 끝자리까지 도달했다면
        return lists # 완성된 2진수를 리턴
    else: # 피벗값이 끝에 도달하지 않았다면 계속 2를 나눠주면서 피벗값이 끝에 도달할때까지 재귀를 돌림
        return deci2bin(s, lists) # 계속 재귀를 돌려줌

b_list = [] # 2진수를 저장할 리스트 배열
Num = int(input("10진수 : ")) # 사용자 입력값 Num 값을 입력받음
deci2bin(Num, b_list) # 함수호출. Num = 사용자 입력, b_list = 2진수를 저장할 리스트. 물론 인자값 자료형을 리스트로만 넘겨주는거지 지역함수에서 사용은 못한다.

b_list.reverse()# 뒤에서부터 순차적으로 구해졌기때문에 역순으로 바꿔주어야함.
b_list = ''.join(map(str, b_list)) # 구해진 리스트를 역순으로 돌렸으니 문자열로 변환
print(b_list)

