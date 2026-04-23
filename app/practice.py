#8000/docs   to get the swagger UI
#8000/redoc

from fastapi import FastAPI 
from typing import Optional
from pydantic import BaseModel

app= FastAPI()


@app.get('/')
def index():
    sr ="hello"
    df={'data':{'name':'nikhil'}}
    return sr
#local host:8000/

@app.get('/about')
def about():
    df1={'data':{'name':'nikhil'}}
    return df1
#local host:8000/about

@app.get('/show/{id}')
def show(id: int):
    #fetch blog with id = id
    df2={'data':id}
    return df2
#local host:8000/show/5


@app.get('/blog/unpublished')
def unpublished():
    df={'data':'all unpublished blogs'}
    return df
#local host:8000/blog/unpublished

'''
@app.get('/blog')
def show():
    df2={'data':'Blog List'}
    return df2
#local host:8000/blog   '''

# @app.get('/blog')
# def blog(limit):
#     df2={'data':f'{limit} blogs of database'}
#     return df2
# #8000/blog?limit=10

@app.get('/blog')
def blog(limit, published):
#def blog(limit, published: bool = True, sort: Optional[str] = None):   #if we want to set default value of published as true and sort as none
#8000/blog?limit=10   0r   8000/blog?published=true

    if published:
        df2={'data':f'{limit} publishedblogs from the database'}
    else:
        df2="published blogs are not shown"
    return df2
#8000/blog?limit=10&published=true
#8000/blog?limit=10&published=false



@app.get('/blog/{id}')
def show(id: int):
    df2={'data':id}
    return df2
#local host:8000/blog/nikhil

@app.get('/blog/{id}/comments')
def comments(id):
    #fetdh comments of blog with id = id
    df4={'data':{"1","2","3"}}
    return df4
#local host:8000/blog/5/comments
#local host:8000/blog/100





class Blog(BaseModel):
    tittle: str
    body: str
    published: Optional[bool] = False

@app.post('/blog')
def create_blog(blog: Blog):
    df5={'data':f'blog is created with tittle as {blog.tittle} and body as {blog.body} and published status as {blog.published}'}
    return df5





# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='127.0.0.1',port=9000)




"""
from fastapi import FastAPI, Depends, HTTPException, status,Response
# from sqlalchemy.orm import Session
# from schemas import Blog, ShowBlog, User, ShowUser
# from models import Blogs,Users
# from database import engine, sessionLocal,get_db
# from typing import List
# from passlib.context import CryptContext
from routers import blog, user,authentication
app=FastAPI()

# Blogs.metadata.create_all(bind=engine)
# def get_db():
#     db=sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog',status_code=201,tags=["Blogs"])  #201 means created
# def create(request: Blog, db: Session= Depends(get_db)):
#     new_blog=Blogs(title=request.title,body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
# def destroy(id, db: Session= Depends(get_db)):
#     blog=db.query(Blogs).filter(Blogs.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
#     db.delete(blog)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
# def update(id,request: Blog, db: Session= Depends(get_db)): 
#     blog=db.query(Blogs).filter(Blogs.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
#     blog.title=request.title
#     blog.body=request.body
#     db.commit()
#     return blog

# @app.get('/blog',response_model=list[ShowBlog],tags=["Blogs"])
# def all(db: Session= Depends(get_db)):
#     blogs=db.query(Blogs).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200,response_model=ShowBlog,tags=["Blogs"])
# def show(id,response:Response, db: Session= Depends(get_db)): 
#     blog=db.query(Blogs).filter(Blogs.id==id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
#         #or --> response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with the id {id} is not available'}
#     return blog

# pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
# @app.post('/users',response_model=ShowUser,status_code=status.HTTP_201_CREATED,tags=["Users"])
# def create_user(request: User, db: Session= Depends(get_db)):
#     hashed_password = pwd_context.hash(request.password[:72])
#     new_user=Users(name=request.name,email=request.email,password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/users',response_model=list[ShowUser],tags=["Users"])
# def all_users(db: Session= Depends(get_db)):
#     users=db.query(Users).all()
#     return users

# # @app.get('/users/{id}',status_code=200,response_model=ShowUser,tags=["Users"])
# # def show_user(id: int,response:Response, db: Session= Depends(get_db)): 
# #     user=db.query(Users).filter(Users.id==id).first()
# #     if not user:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
# #     return user

# @router.get('/{id}',status_code=200,response_model=ShowUser)
# def show_user(id: int,response:Response, db: Session= Depends(get_db)): 
#     user=db.query(Users).filter(Users.id==id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the id {id} is not available')
#     return user

# @app.get('/users/{id}', status_code=200, response_model=ShowUser, tags=["Users"])
# def show_userwithblogs(id: int, response: Response, db: Session = Depends(get_db)): 
#     user = db.query(Users).filter(Users.id == id).first()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f'User with the id {id} is not available'
#         )

#     return user"""