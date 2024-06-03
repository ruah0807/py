

#SET

# 중복을 허용하지 않으며 순서 없이 요소를 저장하는 컬렉션
# 따라서 중복 제거가 필요할 때유용하게 사용할 수 있다.


# { } 중괄호를 사용하여 집합을 생성
ohgiraffers = {'pig', 'squirrel', 'bear', 'gorilla'}

print(ohgiraffers)



# 리스트로 set 생성
another_safari_set = set(['monkey', 'tiger', 'wolf'])

print(another_safari_set)


# 여러타입 허용
mixed_set = {1,'bear', (1,2,3)}
print(mixed_set)




### SET 메소드 ###

# remove( ) : 데이터 삭제
ohgiraffers.remove('pig')
print(ohgiraffers)

# add( ) : 데이터 추가
ohgiraffers.add('piggggg')
print(ohgiraffers)

# 1. update( )
ohgiraffers1 = set(['monkey','tiger','wolf'])
print(ohgiraffers1)

ohgiraffers1.update(['monkey','wolf','tiger','squirrel'])
print(ohgiraffers1)



# 2. discard( ) : 삭제하는 메소드, 데이터가 없더라도 에러를 발생시키지 않음.
ohgiraffers1.discard('pig')

# 3. pop( ) : set은 집합의 순서를 보장하지 않기 때문에 어떤것이 지워질지 알수없다.
ohgiraffers1.pop()
print(ohgiraffers1)


# 4. clear( ) : 모든값을 제거하는 메소드
ohgiraffers1.clear()
print(ohgiraffers1)



# 5. union( ) : 두 set 합집합 (중복은 저장되지않는다.)

javaTeam = {'monkey', 'tiger', 'gorilla'}
pythonTeam = {'pig', 'bear', 'gorilla', 'tiger'}

ohgiraffers2 = javaTeam.union(pythonTeam)
print(ohgiraffers2)




# 6. intersection( ) : 두 set 자료형의 교집합

print(javaTeam.intersection(pythonTeam))


# 7. difference( ) : 좌향을 기준으로 우향의 차집합을 반환한다. 
# pythonTeam 에서 교집합에 속하지 않은것.
print(javaTeam.difference(pythonTeam))


# 8. copy( ) : 대상 set을 복사하여 반환
javaTeam1 = javaTeam.copy()
print(javaTeam1)