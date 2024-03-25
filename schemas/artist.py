from pydantic import BaseModel

class Artist(BaseModel):
    external_url : str | None = None
    num_followers: int | None = None
    genres : list[str] | None = None
    href: str
    id: str
    images : list[dict]
    name:str
    popularity:int
    type:str
    uri : str
    
    