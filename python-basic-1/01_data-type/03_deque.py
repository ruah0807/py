
from collections import deque

# deque : Python의 collections 모듈에서 제공하는 자료구조로써, 
# 양쪽 끝에서 효율적인 삽임과 삭제가 가능하게 설계되었다.

dq = deque()

dq.append('a')
dq.append('b')
dq.append('c')

print(dq)

dq.appendleft('x')
print(dq)


# pop() : 제일 끝에 있는 value 제거
value = dq.pop()
print(value)
print(dq)

# popleft() : 맨쪽에 있는 value 제거
value1 = dq.popleft()
print(value)
print(dq)