from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI
from pydantic import BaseModel

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
def save_post(post):
    print(post)
    return "Recived"