from fastapi import FastAPI, Request, Depends, Form, status
import models
from database import engine, session_local
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse



app = FastAPI()



#sqlalchemy 라이브러리 기능을 이용해 데이터 베이스 테이블 생성
models.Base.metadata.create_all(bind=engine)

# fastAPI 애플리케이션 에서 Jinja2 템플릿 엔진을 사용하도록 설정
templetes = Jinja2Templates(directory='templates')

# 데이터베이스 세션 가져오기
def get_db():
    db = session_local() # 호출 될 때마다 새로운 세션 객체를 생성
    try:
        yield db # 데이터베이스 세션 객체를 반환
    finally:
        db.close()


        
# fastAPI 의 비동기 함수 제공

# 비동기 함수의 장점
# 성능 향상 : 비동기 함수는 여러 작업을 동시에 처리 할 수 있다.
# I/O 작업 (ex) 데이터베이스 쿼리, 외부 api 호출)을 기다리는 동안 다른 작업을 처리할 수 있다.
# 블로킹 방지 : 동기 함수는 한 번에 하나의 작업만 처리하므로, 
#           작업이 끝날 때까지 다른 요청을 처리할 수 없다.


# 비동기 함수를 사용하면 더 많은 클라이언트 요청을 동시에 처리할 수 있다.

@app.get("/") #_________________________________________________
async def home(request : Request, db: Session = Depends(get_db)):
            # Request : HTTP요청 객체를 포함  # depends 키워드로 인해 세션 객체가 먼저 생성됨(db연결)
                   
    # 데이터 베이스에서 Todo 모델을 조회하고, id를 기준으로 내림차순 정렬
    todos = db.query(models.Todo).order_by(models.Todo.id.desc())
    
    # 인덱스 템플릿을 랜더링하여 사용자에게 반환
    return templetes.TemplateResponse("index.html",{'request': request, "todos": todos})




@app.post("/add")               # html 에서 form 태그로 넘겨준 값 
async def add( task:str=Form(...), db:Session=Depends(get_db)):
    
    # todo 클래스의 인스턴스를 생성하고, task 값을 전달하여 할일을 생성
    todo = models.Todo(task=task)
    # 생성한 할 일을 데이터베이스에 추가
    db.add(todo)
    # 변경사항을 커밋
    db.commit()
    
    # 요청이 성공적으로 처리되었으면 리디렉션
    return RedirectResponse(url = app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)



@app.get('/edit/{todo_id}')                   # 선택한 번호를 가져옴
async def add(request:Request, todo_id: int, db: Session = Depends(get_db)):
    
    # 데이터베이스에서 Todo 모델을 가져와, id 가 todo_id와 일치하는 첫 번째 항목을 가져옴
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    # 템플릿을 랜더링 하여 사용자에게 반환
    return templetes.TemplateResponse("edit.html", {"request" : request, "todo" : todo})



@app.post("/edit/{todo_id}")
async def add(todo_id:int, task:str = Form(...), completed:bool = Form(False), db:Session=Depends(get_db)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    #todo task 속성을 폼에서 받아온 값으로 업데이트
    todo.task = task
    # todo 의 completed 속성을 폼에서 받아온 completed 값으로 업데이트
    todo.completed = completed
    
    db.commit()
    
    # 홈으로 리디렉션
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{todo_id}")
async def delete(todo_id:int, db:Session = Depends(get_db)):
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    db.delete(todo)
    
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)