temp = int(input("온도를 입력하세요: "))

if(temp < 0):
    state = "얼음"
else:
    state = "기체"
print(state)

# print가 중복이 되어서 모든 조건문이 끝난 후에 출력함.