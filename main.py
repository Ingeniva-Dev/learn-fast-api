from sre_constants import ANY
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "i like pizza", "id": 2}]

def find_post():
    for p in my_posts:
        if p[""] == id:
            return p


@app.get("/")
def root():
    return {"data": my_posts}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000000)
    my_posts.append(post.dict)
    return {"data": post_dict}
    #print(post.rating)
    #print(post.dict())

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return {"post_detail": post}



