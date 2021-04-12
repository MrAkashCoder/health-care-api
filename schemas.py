from pydantic import BaseModel
from typing import List, Optional


class Post(BaseModel):
    id: int
    title: str
    short_description : str
    # description : str
    category_id: str
    # author_id: str
    date : str
    # viewer_count: int
    post_url : str
    image_URL : str
    # tags : str
        

class User(BaseModel):
    name : str
    email : str
    password : str

class ShowUser(BaseModel): 
    name : str
    email : str
    # posts : List[Post]
    class Config():
        orm_mode = True

class ShowPost(Post):
    pass
    # title: str
    # short_description : str
    # category_id: str
    # date : str
    # post_url : str
    # image_URL : str
    # creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel): 
    username: Optional[str]= None