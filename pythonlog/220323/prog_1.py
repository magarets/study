def ModNumber(x, y):
    if(x % y == 0): #x가 y로 나눠지는지??
        return True #나눠지면 true 반환

x = int(input("정수를 입력하시오 : ")) # 첫 번째 정수
y = int(input("정수를 입력하시오 : ")) # 두 번재 정수

if(ModNumber(x, y)): # ModNumber 함수에서 나머지를 검사해서 반환값이 True이면 참
    print("약수 입니다")
else: # True값이 아니면 거짓
    print("약수가 아닙니다")