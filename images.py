import requests,os, shutil
from config import settings
import users

def check_folder_valid(folder_name:str):
    assert len(folder_name) >= 1
    return check_folder_valid != ''

def check_folder_exists(folder_name:str):
    folder_valid = check_folder_valid(folder_name)
    if os.path.exists(folder_name):
        return True
    return False

def create_folder(folder_name:str):
    if check_folder_exists(folder_name):
        shutil.rmtree(folder_name)
    
    os.makedirs(folder_name)
    return True
    

def upload_images(url:str,folder_name:str,artist_name:str="artist",id:str="1", size:int = 320):

    file_name = os.path.join(folder_name,f'{artist_name}_{id}_{size}.png')
    res = requests.get(url=url)
    if res.status_code == 200:
        
        with open(file_name,"wb") as f:
            f.write(res.content)
        return True
    return False
        

def upload_your_top_artists_images(folder_name:str):
    created_folder = create_folder(folder_name)
    artists = users.get_my_top_items(type="artists")["artists"]
   
    for artist in artists:
        image_dir = os.path.join(folder_name,f'{artist["name"]}')
        os.makedirs(image_dir, exist_ok=True)
        for image in artist["images"]:
            upload_images(url=image["url"], folder_name=image_dir, artist_name=artist["name"], id = artist["id"], size=image["height"])
    
    