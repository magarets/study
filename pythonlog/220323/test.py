import random

computer_choice = random.randint(1, 3)
user_choice = int(input("어디를 공격하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)"))

if computer_choice == user_choice:
    print("수비에 막혔습니다. ")
else:
    print("페날티킥이 성공하였습니다. ")