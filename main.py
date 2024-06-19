from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True,
    rating: Optional[int] = None


my_posts = [
    {'id': 1, 'title': 'Post 1', 'content' : 'Content 1'},
    {'id': 2, 'title': 'Post 2', 'content': 'Content 2'}
]




@app.get("/")
async def root():
    return {"message" : "Welcome to my API!!!"}



@app.get("/posts")
def get_posts():
    return {"data" : my_posts}

@app.post("/posts")
def create_post(new_post: Post):
    post_dict = new_post.model_dump()
    post_dict["id"] = randrange(3,1000000)
    print(post_dict)
    my_posts.append(post_dict)
    return {"message" : post_dict}
