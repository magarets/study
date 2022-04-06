""" python function
import math
x = int(input("첫 번째 정수 : "))
y = int(input("두 번째 정수 : "))
print(math.gcd(x, y))
"""

def gcd_a(minNum, maxNum): # minNum = 입력값중 작은값, maxNum = 입력값중 큰값
    max = -1 # 최댓값을 구하는 변수 초기화
    for i in range(1, minNum+1): # 둘중 작은수를 기준으로 값을찾아서 범위를 줄임
     if(maxNum % i == 0 and minNum % i == 0): # 두개의 수랑 기준이되는 1~minNum까지 전부 나눠서 나머지를 구해서 공통된 약수를 찾음. (Brute force)
         if(i > max): # 최근 약슨값보다 찾은 약수가 더 클때
             max = i # max에 약수 업데이트
    return max # 제일 큰 약수를 리턴


x = int(input("첫 번째 정수 : ")) # 첫번째 정수 입력
y = int(input("두 번째 정수 : ")) # 두번째 정수 입력

print(gcd_a(min(x, y), max(x, y)))
