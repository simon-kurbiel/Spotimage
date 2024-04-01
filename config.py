from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    CLIENT_ID:str
    CLIENT_SECRET:str
    REDIRECT_URI:str
    AUTHORIZATION_URL:str="https://accounts.spotify.com/authorize"
    SCOPES:str="user-top-read user-read-private user-read-email"
    UPLOAD_FOLDER: str = "uploads"
    
    class Config:
        env_file='.env'
        
settings = Settings()


