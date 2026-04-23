
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas import Blog, ShowBlog, User, ShowUser
from passlib.context import CryptContext
from typing import List
from app.database import get_db
from app.models import Users


router=APIRouter(
    tags=["Users"],
    prefix="/user"
)


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
@router.post('/',response_model=ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session= Depends(get_db)):
    hashed_password = pwd_context.hash(request.password[:72])
    new_user=Users(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/',response_model=list[ShowUser])
def all_users(db: Session= Depends(get_db)):
    users=db.query(Users).all()
    return users



@router.get('/{id}', status_code=200, response_model=ShowUser)
def show_userwithblogs(id: int, response: Response, db: Session = Depends(get_db)): 
    user = db.query(Users).filter(Users.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with the id {id} is not available'
        )

    return user








