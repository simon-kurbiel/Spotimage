import auth
import requests

import schemas.artist as artist_schema



def get_artist_data(id:str, token:dict = auth.token):
    """ Get a single artist data """
    url = f'https://api.spotify.com/v1/artists/{id}'
    res = requests.get(url=url, headers=token)
    if res.status_code != 200:
        return "FAILED"
    res_json = res.json()
    num_followers = res_json["followers"]["total"]
    external_url = res_json["external_urls"]["spotify"]
    data = artist_schema.Artist(**res_json, num_followers=num_followers, external_url=external_url)
    return data.dict()

def search_for_artist(name:str, limit:int=1, token:dict = auth.token):
    """Get all the artists matching the query"""
    
    url = "https://api.spotify.com/v1/search"
    search_query = {"q":name, "type":"artist", "limit":limit}
    res = requests.get(url=url, params=search_query, headers=token)
    if res.status_code != 200:
        return "FAILED"
    res_json = res.json()
    artists = res_json["artists"]["items"]
    all_artists = [get_artist_data(id=artist["id"]) for artist in artists ]
    return all_artists
     


print(get_artist_data(id="4Z8W4fKeB5YxbusRsdQVPb"))
# print(search_for_artist(name="Kanye West", limit=1))
