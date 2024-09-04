
# 요청 응답

# POST, PUT, PATCH 등의 메소드를 사용하는 경우 HTTP 본문(body)사용

# 단순 텍스트나 json을 이용한다.

# pydantic 으로 요청 본문 받기
# 데이터 유효성 검사 및 설정 관리를 위한 라이브러리

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl


app = FastAPI()


# UserInfo 클래스(BaseModel을 상속받음)
# BaseModel을 상속 받아야 request body 부분을 받을 클래스로 이용가능하다.
class UserInfo(BaseModel) :
    name : str
    password : str
        # url은 선택사항이며, URL 형식으로 받아와야한다. 기본값은 None이다.
    url : Optional[HttpUrl] = None


# /users post 요청에 담아온 body 부분을 userInfo 자료형에 담아 user라는 객체를 생성
@app.post("/users")
def create_user(user : UserInfo):
    return user


