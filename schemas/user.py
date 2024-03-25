from pydantic import BaseModel
import schemas.artist as artist_schema
class UserInfo(BaseModel):
    display_name:str
    id:str
    images:list
    uri:str
    type:str
    num_followers:int = 0
    
class TopItemsBase(BaseModel):
    type:str
    total:int
    
class TopItemsArtists(TopItemsBase):
    artists : list[artist_schema.Artist]
    pass
    
    
    
    