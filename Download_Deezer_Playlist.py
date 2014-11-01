import requests
import json
import sys

from  grooveshark import Client


client=Client()
client.init()

#On passe l'id de l'utilisateur en paramètre
userid=sys.argv[1]
tracks_count=0

user_playlists=json.loads(requests.get("http://api.deezer.com/user/" + str(userid) + "/playlists").text)['data']

for playlist in user_playlists:
  
  json_result=requests.get("http://api.deezer.com/playlist/" + str(playlist['id']))
  playlist_tracks=json.loads(json_result.text)['tracks']['data']
  
  for track in playlist_tracks:
    
    try:
      song=list(songs)[0]
      song.download()
      tracks_count+=1
    except:
      pass

print str(tracks_count) + " tracks downloaded"