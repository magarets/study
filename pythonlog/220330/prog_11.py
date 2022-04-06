max = -1 # 최댓값을 구하기위한 변수 초기화

x = int(input("첫 번째 정수를 입력하시오 : "))
y = int(input("두 번째 정수를 입력하시오 : "))

for i in range(1, min(x,y)+1): # 두 수중에 가장 작은수를 기준으로 범위를 설정
    if((x % i == 0) and (y % i == 0)): # x와 y를 i로 나눴을 때 모두 나머지가 0인경우
        if(max < i): # 이때의 i값이 현재 max에 저장된 값보다 크면
            max = i # max 값 업데이트
print(f"{x} 와 {y}의 최대 공약수는 {max} 입니다.")