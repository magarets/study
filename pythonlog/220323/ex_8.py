heated = False
if(heated == False):
    print("난방이 가동되지 않았음")

heated = True
if not heated:
    print("난방이 가동되지 않았음")

# 가독성이 높은건 if문에 '어떨 때 아래 수행문을 수행할지'를 직관적으로 알 수 있는첫번째 if문이다.
# 두번째 if문은 heated 불룬변수의 초기값을 모르므로, not 을 하였을 때 어떤값이 나오는지 모르기 때문임.