

# Dictionaries : 자바의 map과 같은 원리

# 키와 값의 쌍으로 구성된 데이터 구조로, 키를 통해 값을 찾을 수있으므로, 매우 빠른 조회 성능을 보여준다.

         # 'key':'value'
teacher = {'name': 'pig', 'team':'ohgiraffers'}

print(type(teacher))
print(teacher['name'])


# 생성 후 키-값 추가/수정/삭제
teacher['age'] = 20
print(teacher['age'])

# in 키워드 : 키값의 존재 여부 확인 true/false
print('name' in teacher)


# 1. get( ) 
# 배개변수로 전달받은 key에 해당하는 값을 반환
print(teacher.get('name'))

# 2. keys( ) : 모든 키값을 반환
print(teacher.keys())

# 3. values( ) : 모든 value값을 반환
print(teacher.values())

# 4. items( ) : 모든 keys와 values반환
print(teacher.items())
print(teacher)

# 5. pop( ) : key 내용 제거 메소드
print(teacher.pop('age')) # 삭제할 value값 반환(출력)
print(teacher)

# 6. clear( ) : 모든 항목 제거
teacher.clear()
print(teacher)