

### if 문 ###


재고량 = 20

if 재고량 > 0 : 
    print('지금 주문가능합니다.')
    

중고차재고 = [ 'K5', 'BMW', 'Benz' ]
if 'K6' in 중고차재고 :
    print('재고 있습니다.')
else : 
    print('주문불가능합니다.')







### For 문 ###


for i in range(0,3) :
    print('k5 있어요')
    

중고차들 = ['Tico', 'Lexus', 'Mustang']

for i in 중고차들 :
    print(i * 3)







### 함수 문법 Def : definition의 약자 (긴코드 줄이고싶을때) ###

def greeting():
    print('안녕하세요 무섭게 성장하는 신입개발자 김루아입니다^^')

greeting()



def hat(empty, empty2) :
    print(empty * empty2)

hat(1,4)
hat(3,6)


def 함수() :
    return 10

print(함수())