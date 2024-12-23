from pydantic import BaseModel
from typing import List

class URLInput(BaseModel):
    urls: List[str]
    query: str

class TwitterThread(BaseModel):
    tweets: List[str]
    
class TwitterResponse(BaseModel):
    thread: TwitterThread
    status: str 