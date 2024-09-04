

# List

# 일련의 값이 모인 집합을 다루기 위한 자료형
# 일반적인 프로그래밍 언어와 다르게 길이를 동적으로 조절할 수 있어, list라고 부른다.
# 파이썬은 배열이 List.

fruits = ['orange', 'apple', 'pear', 'kiwi', 'banana', 'apple']

print(fruits)
print(fruits[2])



## List 유용한 메소드 ##

### 1. count() : 해당 리스트에 인자로 준 값이 몇 개 존재하는지 확인하여 그 수를 반환.
print("apple: ", fruits.count('apple'))




### 2. index() : 인자로 준 값이 몇 번째 인덱스에 존재하는지 확인하여 그 인덱스를 반환

# 같은 값이 리스트 내에 여러 개 존재하면 가장 처음에 존재하는 값의 인덱스를 반환
print('index: ', fruits.index('apple'))

# 3번째 이후의 'apple'을 탐색하겠다는 의미
print('index: ', fruits.index('apple', 3)) 




### 3. reverse() : list 값을 역으로 정렬
fruits.reverse()
print(fruits)



### 4. append() : list 끝에 값을 덧붙여 추가
fruits.append('pineapple')
print(fruits)


### 5. sort() : 요소를 정렬하는 메소드로 원본 list에 영항을 준다.

# 기본적으로 알파벳 첫 글자를 기준으로 오름차순 정렬
fruits.sort()
print(fruits)

# 내림차순 정렬
fruits.sort(reverse=True)
print(fruits)

# length 가 짧은 순으로 정렬
fruits.sort(key=len)
print(fruits)

# length 가 짧은 순으로 정렬 및 역순 출력
fruits.sort(key=len, reverse=True)
print(fruits)





### 6. del 키워드

# 원본 배열 일부 요소 혹은 전체 목록 제거 가능
abclist = ['A', 'B', 'C', 'D', 'E', 'F']
print(abclist)

del abclist[0]
print(abclist)


# 1번째부터 3번째 '전까지' 제거
del abclist[1:3]
print(abclist)

#자체리스트 제거
del abclist
# print(abclist) -- 지웠기때문에 출력 불가


