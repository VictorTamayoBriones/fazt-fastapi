from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4 as uuid

app = FastAPI()

posts = []

#Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return {"welcome":"Welcome to my Rest API"}

#Obtener los posts
@app.get('/posts')
def get_posts():
    return posts

#Save post
@app.post('/post')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

#Obtener un post por ID
@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")