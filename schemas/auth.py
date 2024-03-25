from pydantic import BaseModel
from config import settings
class AuthorizationCode(BaseModel):
    grant_type:str = "authorization_code"
    code:str
    redirect_uri:str
    client_id:str
    client_secret:str
    