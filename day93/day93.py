# import requests, json, os
# from requests.auth import HTTPBasicAuth

# clientID = os.environ['CLIENT_ID']

# clientSecret = os.environ['CLIENT_SECRET']

# artist = input("Artist: ").lower()
# artist = artist.replace(" ","%20")

# url = "https://accounts.spotify.com/api/token"

# data = {"grant_type":"client_credentials"}

# auth = HTTPBasicAuth(clientID, clientSecret)

# response = requests.post(url, data=data, auth=auth)

# #print(response.ok)
# #print(response.json())
# #print(response.status_code)

# accessToken = response.json()["access_token"]
# url = "https://api.spotify.com/v1/search"
# headers = {'Authorization': f"Bearer {accessToken}"}
# #search = "?q=artist%3Aqueen&type=track&limit=5"
# search = f"?q=artist%3A{artist}&type=track&limit=5"

# fullURL = f"{url}{search}"
# #print(fullURL)

# response = requests.get(fullURL, headers=headers)
# data = response.json()

# #print(json.dumps(data, indent=2))

# for track in data["tracks"]["items"]:
#   print(track["name"])
#   #print(json.dumps(data, indent=2))
#   print(track["preview_url"])









from flask import Flask, request
import os, requests, json
from requests.auth import HTTPBasicAuth
from replit import db


def getTracks(year):
  clientID = os.environ['CLIENT_ID']
  clientSECRET = os.environ['CLIENT_SECRET']
  
  url = "https://accounts.spotify.com/api/token"
  data = { "grant_type": "client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSECRET)
  
  response = requests.post(url, data=data, auth=auth)
  
  #print(response.json())
  accessToken = response.json()["access_token"]
  
  #year = 1990
  offset = 0
  try:
    offset = db[year]
    if offset >200:
      db[year] = 0
    db[year] += 10
  except:
    db[year] = 10
  
  headers = {"Authorization": f"Bearer {accessToken}"}
  url = "https://api.spotify.com/v1/search"
  search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"
  
  fullURL = f"{url}{search}"
  print(fullURL)
  
  response = request.get(fullURL, headers=headers)
  data = response.json()
  #print(data)

  songs = ""
  file = open("songs.html", "r")
  songs = file.read()
  file.close()

  listSongs = ""
  
  for track in data["tracks"]["items"]:
    thisTrack = songs
    thisTrack = track.replace("{name}",f"""{track["name"]} by {track["artists"][0]["name"]}""")
    #print(f"""{track["name"]} by {track["artists"][0]["name"]}""")
    track = track.replace("{url}",track["preview_url"])
    listSongs += thisTrack

  return listSongs
    #print(track["preview_url"])
  
app = Flask(__name__)



@app.route("/", methods=["POST"])
def change():
  page = ""
  file = open("form.html", "r")
  page = file.read()
  file.close()
  year = request.form["year"]
  songs = getTracks(year)
  page = page.replace("{songs}", songs)
  page = page.replace("{value}", year)
  return page


@app.route("/")
def index():
  page = ""
  file = open("index.html", "r")
  page = file.read()
  file.close()
  page = page.replace("{songs}", "")
  page = page.replace("{value}", "1990")
  return page


app.run("0.0.0.0", port=81)