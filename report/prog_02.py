myList = [ 11, 22, 23, 99, 81, 93, 35 ] # myList라는 리스트를 생
sum = 0 # sum이라는 정수의 합을 누적하는 변수 생성. 누적해야하기에 초기값을 0으로 설정하였음

for num in myList: # myList의 0번째부터 6번째까지 한번에 하나의 값이 num으로 들어감.
    sum += num # myList의 리스트값이 하나씩 저장되는 num변수의 값을 sum에 누적

print(f"정수들의 합은 {sum}")