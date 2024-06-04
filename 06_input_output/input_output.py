
# 입출력

### file open 종류 ###
# 1. r = 읽기 모드. 파일을 읽기만 할 때 사용
# 2. w = 쓰기 모드. 파일에 내용을 쓸 때 사용 / 해당 파일이 존재하지 않으면 새로운 파일이 생성
# 3. a = 추가 모드. 파일의 마지막에 새로운 내용을 추가할 때 사용
# 파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고
# 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.


f = open('newfile.txt', 'w')
f.close()

# C: higangnam/test
f = open("/Users/ruahkim/higangnam/test/newfile.txt", 'w')
f.close()


# 파일을 쓰기ㅣ 모드로 열어서 내용 쓰기
f = open('/Users/ruahkim/higangnam/test/newfile.txt', 'w')
for i in range(1,11) :
    data = '%d 번째 줄입니다.  \n' % i
    f.write(data)
f.close()




# 파일을 읽는 방법

# 1. readline 사용하기 : 파일의 첫번째 줄을 읽어서 출력
f = open('/Users/ruahkim/higangnam/test/newfile.txt','r')
line = f.readline()
print(line)
f.close()

# 2. 반복문 이용 모든 내용 읽기
f = open('/Users/ruahkim/higangnam/test/newfile.txt', 'r')
while True:
    line = f.readline()
    if line == '':
       break
    print(line) 
f.close()

print('----------------------------------')


# 3. 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
f = open('/Users/ruahkim/higangnam/test/newfile.txt', 'r')
lines = f.readlines() 
for line in lines : 
    print(line)
f.close()

print('----------------------------------')

# 4. for 문 자체 사용
f = open('/Users/ruahkim/higangnam/test/newfile.txt', 'r')
for line in f :
    print(line)
f.close()


print('----------------------------------')


# 5. 파일에 새로운 내용 추가하기
f = open('/Users/ruahkim/higangnam/test/newfile.txt', 'a')
for i in range(11,15) :
    data = '%d 번째 줄입니다. \n' % i
    f.write(data)
f.close()


print('----------------------------------')


# 6. with 문
# 파일을 열면 항상 닫아 주어야한다. (open -> close)
# 이렇게 파일을 열고 닫는 것을 자동으로 처리하는 역할을 with 문이 해준다.
# with문은 저절로 close가 된다.
with open('newfile2.txt','w') as f :
    f.write("Lif is too short, you need more enjoy your life.")