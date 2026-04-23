from fastapi import FastAPI, Depends, HTTPException, status,Response
from app.database import engine
from app import models
from app.routers import blog, user,authentication
app=FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "FastAPI running 🚀"}