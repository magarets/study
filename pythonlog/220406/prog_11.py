def deci2bin(num, lists):
    s = num // 2
    r = num % 2
    lists.append(r)

    if(s == 0):
        return lists
    else:
        return deci2bin(s, lists)

b_list = []
result_1 = []
Num = int(input("10진수 : "))
answer = deci2bin(Num, b_list)
result_1 = answer
result = ''.join(result_1)
print(result)

