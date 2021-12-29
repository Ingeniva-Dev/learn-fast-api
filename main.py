from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favoriate foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post():
    for i, p in enumerate(my_posts):
        if p[''] == id:
            return i


@app.get("/")
def root():
    return {"message": "hello its my api"}

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    print(post)
    print(post.dict())

    my_posts.append(post.dict())
    return{"data": post_dict} 

@app.get("/posts/{id}")
def get_post(id: int, response: Response):

    post = find_post(id)
    if not post: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'message': f"post with id {id} was not found"}

    print(id)
    return{"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int):
    # deleting post
    # find index in the array that has required ID
    # my_posts.pop(delete)
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


