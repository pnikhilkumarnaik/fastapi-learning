from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import Login
from app.models import Users
from app.hashing import Hash
from app.dependencies.jwttoken import create_access_token
from app.database import get_db
from fastapi.security import OAuth2PasswordRequestForm


router=APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user=db.query(Users).filter(Users.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with the email {request.username} is not available')
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f'Incorrect password')
     
    #generate token and return
   
    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}