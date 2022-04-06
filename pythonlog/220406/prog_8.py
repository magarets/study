def num2word(number): # 숫자에 해당하는 문자를 리턴하는 함수. 예를들어 123에서 [2]가 들어왔을때 '이'을 리턴함
    wordlist = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return wordlist[int(number)-1] # 인덱스는 0부터시작하므로 매개변수에서 -1 한값번째의 인덱스값을 리턴해준다.

def getMoneyText(x): # 사용자가 입력한 숫자를 문자로 바꿔주는 함수
    word_list = ['원', '십', '백'] # word_list : 단위를 나타내는 리스트
    input_list = list(map(int, str(x))) # text_list : 사용자로부터 입력받은 x를 (str)로 형변환을 해준뒤, list로 만들어서 input_list에 저장
    Lresult= list() # 최종 결과값을 저장할 리스트 생성

    for i, v in enumerate(input_list): #i = index( 0 ~ len(input_list) ), v = input_list[i]
        getword = num2word(v) #숫자를 문자로치환하는 함수를 getword에 저장. v = input_list[i]
        Lresult.append(getword) # 바로 윗줄에서 구한 값을 Lresult 뒤에 붙이기
        Lresult.append(word_list[ len(input_list)- i - 1 ]) # 최종길이 len(input_list)에 1을빼준뒤, i(현재 for의 index)를 빼면 최종길이가 몇이든 상관없이 word_list의 리스트 인덱스값이 나오게 된다.
    Lresult = ''.join(Lresult) # 공백제거
    print(Lresult)


x = int(input("1000이하의 숫자를 입력하시오 : ")) # 사용자 입력값
getMoneyText(x) # 문자로 출력해주는 함수 호출


