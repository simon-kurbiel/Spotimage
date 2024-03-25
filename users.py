import schemas.artist as artist_schema
import schemas.user as user_schema
import auth
import requests, json

def get_my_top_items(type:str="artists", token:str = auth.token):
    url = f'https://api.spotify.com/v1/me/top/{type}'
    res = requests.get(url=url, headers=token)
    
    
    res_json = res.json()
    res_items = res_json["items"]
    all_artists = []
    if type == "artists":
        all_artists = [artist_schema.Artist(**item, num_followers=item["followers"]["total"], external_url=item["external_urls"]["spotify"]) 
                       for item in res_items]
    
        return user_schema.TopItemsArtists(type="artist", total=res_json["total"], artists=all_artists).dict()
      
    
        
        
    return res.json()
  