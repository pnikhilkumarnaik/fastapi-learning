from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response
from app.database import get_db
from app.models import Blogs
from app.schemas import Blog

def get_all(db: Session):
    blogs=db.query(Blogs).all()
    return blogs

def create_blog(request: Blog, db: Session= Depends(get_db)):
    new_blog=Blogs(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy_blog(id, db: Session= Depends(get_db)):
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT),"deleted successfully"

def update_blog(id,request: Blog, db: Session= Depends(get_db)): 
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.title=request.title
    blog.body=request.body
    db.commit()
    return "updated successfully"

def show_blog(id,response:Response, db: Session= Depends(get_db)): 
    blog=db.query(Blogs).filter(Blogs.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        #or --> response.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
    return blog