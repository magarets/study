import math # pow 함수를 쓰기위해 math 라이브러리 import

def get_peri(radius = 5): # 원의 둘레를 구하는 함수. 파라미터가 없다면 기본함수인자값은 5로 설정
    return math.pow(radius, 2) * 3.14 # pow(radius, 2) => radius 의 2승에 파이값인 3.14를 곱해서 원의 둘레를 구해서 리턴

Uinput = input(f"get_peri() = ") # 사용자값 입력

if(Uinput): # 입력값이 존재한다면
    print(get_peri(float(Uinput))) # 입력값이 존재하면 함수실행
else:
    print(get_peri()) # 입력값이 없다면 null 일때는 인자값을 안주고 함수만 호출
