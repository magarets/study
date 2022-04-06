def getMoneyText(x):
    word_list = ['', '백', '십', '원']
    text_list = list(x)
    last_text = ''
    for cnt in range(len(text_list), 0, -1):
        print(text_list[cnt-1], word_list[cnt])
        last_text += word_list[cnt] + text_list[cnt-1] + ' '
    a = list(last_text)
    a.reverse()
    b = ''.join(a)
    print(b)


x = input("1000이하의 숫자를 입력하시오 : ")
getMoneyText(x)


