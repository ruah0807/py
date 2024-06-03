

# if 문

# if 조건식 : 
#   실행 내용

x = int(input("정수 하나를 입력해주세요 : "))

if x > 0 :
    print('입력하신 %d는 양수입니다. ' % x)
    
elif x==0 :
    print('입력하신 %d는 zero입니다.' % x)
else :
    print('입력하신 %d는 음수입니다.' % x)
    


# match 문 (자바의 swich)
# 주어진 값을 case 블록의 값과 비교해 일치하는 case 만 실행

print("====== vending marchine ======")
print(" milkiss(500) coke(600) fanta(700) milkiss(1000)")
print("원하시는 음료를 선택해주세요 : ")

drink = input()

price = 0
match drink:
    case "sider":
        print("사이다를 선택하셨습니다.")
        price = 500
    case "coke":
        print("콜라를 선택하셨습니다.")
        price = 600
    case "fanta":
        print("환타를 선택하셨습니다.")
        price = 700
    case "milkiss":
        print("밀키스를 선택하셨습니다.")
        price = 1000
    case _:
        print("저희가 제공하는 음료수가 아닙니다.")
        
print(str(price) + "원을 투입해주세요")

    