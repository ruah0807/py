

# 함수

# def 키워드를 사용해 함수를 정의하고 함수 이름 다음에 괄호와 클론을 작성

# def function() :
#       함수가 실행하는 코드 내용

def myfunction():
    print('hello world')
    
myfunction()



def addNum(num1,num2):
    print(num1+num2)
    
addNum(2,4)




def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)


### 인자로 보내는 방법 2가지 ###
#    1. 위치 인자 = 위치로 매칭하는 방법
#    2. 키워드 인자 = 매개변수 이름으로 매칭

def func(a,b):
    print(a,b,sep=" ")
    
# 1. 위치 매칭
func('hello','world')

# 2. 키워드 매칭(순서 관계없음)
func(b='world', a='hello')



## 매개변수 기본 값 지정
def func2(a, b=3):
    return a+b

print(func2(10,10))
print(func2(10)) # 기본값 b의 3이 적용되어 출력.



# pakage : 많은 인자를 하나로 묶어 버림 

def add_many(*args):
    result = 0
    for i in args : 
        result = result + i
    return result 

print(add_many(1,2,3,4,5,5,6,7,8,9,10))




# unpakage : 
def sum(a,b,c):
    return a+b+c
numbers = [1,2,3]
print(sum(*numbers))





# Lamda 표현식

# 매개 변수로 함수를 전달하기 위해 함수 구문을 사용하는 것이 번거롭고 
# 코드 낭비라고 생각 될때 함수를 간단하고 쉽게 선언하는 방법

# 람다 기본식 예시
add = lambda x,y : x + y
print(add(3,5))

numbers1 = [1,2,3,4,5]

squard_numbers = map(lambda x: x**2, numbers1)
print(list(squard_numbers))



# 조건에 맞는 요소 필터링
# 2로 나누었을 때 나머지가 0이 되는 값
numbers2 = [1,2,3,4,5,6]
even_number = filter(lambda x : x % 2 == 0, numbers2)
print(list(even_number))


# 정렬
points = [(1,2),(3,1),(5,-1)]
sorted_points = sorted(points, key=lambda x: x[1])
# [1]번째 인덱스 오름차순으로 정렬 : -1 -> 1 -> 2
print(sorted_points)




