

from pydantic import BaseModel, Field
from typing import List

class BaseBlog(BaseModel):  
    title: str
    body: str
class Blog(BaseBlog):
    class Config():
        from_attributes = True
    

class User(BaseModel):
    name: str
    email: str
    password: str 



class ShowUser(BaseModel):
    name: str
    email: str
    blogs:  List[Blog] =[]#we want to show all the blogs of a user in a response
    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
    #title: str --> we only see title in a respose
    #body: str --> we only see body in a respose
    #what we want to show in a response
    class Config:
        from_attributes = True
    
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None
