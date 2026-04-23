from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.dependencies import oauth2
from app.dependencies.oauth2 import get_current_user
from app.schemas import Blog, ShowBlog, User, ShowUser
from typing import List
from app.database import get_db
from app.models import Blogs
from app.repository.blog import create_blog, destroy_blog, get_all,update_blog,show_blog
router=APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)

@router.get('/',response_model=list[ShowBlog],tags=["Blogs"])
def all(db: Session= Depends(get_db),current_user: User= Depends(get_current_user)):
    
    return get_all(db)

@router.post('/',status_code=201,tags=["Blogs"])  #201 means created
def create(request: Blog, db: Session= Depends(get_db),get_current_user: User= Depends(get_current_user)):

    return create_blog(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session= Depends(get_db),get_current_user: User= Depends(get_current_user)):
   
    return destroy_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request: Blog, db: Session= Depends(get_db),get_current_user: User= Depends(get_current_user)): 
   
    return update_blog(id,request,db)

@router.get('/{id}',status_code=200,response_model=ShowBlog)
def show(id,response:Response, db: Session= Depends(get_db),get_current_user: User= Depends(get_current_user)): 
    
    return show_blog(id,response,db)