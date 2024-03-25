from config import settings
import schemas.auth as auth_schema
import schemas.user as user_schema
import requests



def get_token():
    
    print('visit this url to grant access:')
    print(f"{settings.AUTHORIZATION_URL}?client_id={settings.CLIENT_ID}&redirect_uri={settings.REDIRECT_URI}&response_type=code&scope={settings.SCOPES}")

    authorization_code = input("Enter the authorization code here : ")
    data = auth_schema.AuthorizationCode(code=authorization_code, redirect_uri=settings.REDIRECT_URI, client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET).dict()
    
    token = requests.post(
                            url='https://accounts.spotify.com/api/token', 
                            headers={"Content-Type":"application/x-www-form-urlencoded"},
                            data= data
                        )
 
  
        
    return token.json()

def get_auth_token():
    access_token=  get_token()['access_token']
   
    auth_token = {"Authorization" : f'Bearer {access_token}'}
    return auth_token

token = get_auth_token()

def get_my_profile(token:dict):
    url = "https://api.spotify.com/v1/me"
    res = requests.get(url=url, headers=token)
    if res.status_code != 200:
        return "FAILED"
    res_json = res.json()
    num_followers = res_json["followers"]["total"]
    profile = user_schema.UserInfo(**res_json, num_followers=num_followers)
    return profile.dict()

def get_my_id():
    return get_my_profile(token=token)["id"]

