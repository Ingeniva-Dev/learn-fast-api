from typing import Optional
import dotenv
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

USER="postgres"
PASSWORD="XXXXXXXX"

while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database='fastapi', user=USER, password=PASSWORD)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("connecting to DB failed")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favoriate foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "hello its my api"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    # print(posts)
    return{"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    
            (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    # post_dict = post.dict()
    # ost_dict['id'] = randrange(0, 10000000)
    # print(post)
    # print(post.dict())
    conn.commit()

    # my_posts.append(post.dict)
    return{"data": new_post} 

@app.get("/posts/{id}")
def get_post(id: int, response: Response):

    post = find_post(id)
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'message': f"post with id {id} was not found"}

    print(id)
    return{"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find index in the array that has required ID
    # my_posts.pop(delete)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
   # print(post)
    index = find_index_post(id)

    if index == None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}
    #return {'message': "updated post"}



