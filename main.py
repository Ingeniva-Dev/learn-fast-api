from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message": "hello its my api"}

@app.get("/posts")
def get_posts():
    return{"data": "This is your posts"}

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post.rating)
    print(new_post.dict())
    return{"data":"new post"} 

