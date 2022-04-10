ID = "daegu" # ID 값에는
Password = "university"
UserID = ""
UserPasswd = ""

while(UserID != ID):
    UserID = input("아이디를 입력하시오 : ")
    if(UserID == ID):
        while(UserPasswd != Password):
            UserPasswd = input("암호를 입력하시오 : ")
print("로그인 성공")