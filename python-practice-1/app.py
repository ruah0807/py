print('Ruah Kim')
print(100+100)
print('ruah kim' * 20)

이름 = '김루아와 조성우는 최고의 개발자가 될것이다. 음하하핳하'
print(이름[0])
print(이름[0:6])


secondHand = ['Benz S Slass', 'black', [5000, 8000]]
print(secondHand[0])
print(secondHand[1])

secondHand[1] = 'white'
print(secondHand[1])


# 자료 수정하는 법 

# secondHand.sort()  // 숫자+문자 순으로 정렬
# secondHand.reverse() //뒤집음
# secondHand.pop()  // 맨뒤에 자료를 가져욤

print(secondHand.pop())

# Dictionary 라는 자료형
secondHand2 = {
    'Brand' : 'BMW', 
    'Model' : '520d' 
    }  
print(secondHand2['Brand'])

