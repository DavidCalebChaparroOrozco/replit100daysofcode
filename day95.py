import requests, os, json
from requests.auth import HTTPBasicAuth

country = "IN"

def getnews(max):
  newsapi = os.environ["news"]
  url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsapi}"
  result = requests.get(url)
  data = result.json()
  # print(json.dumps(data, indent=2))

  count = 0
  for article in data['articles']:
    if article['content']:
      count += 1
    else:
      continue
    if count > max:
      break

    print(f"News #{count}:")
    #print(article['title'])
    #print(article['url'])
    print(article['content'])

    prompt = "Give me three summary words from the following text: "
    prompt += article['content']
    summary = ai21_prompt(prompt)
    print(f"Summary words: {summary}")
    getSpotifyTrack(summary)
    print()

def ai21_prompt(prompt):
  ai21key = os.environ['ai21key']

  url = "https://api.ai21.com/studio/v1/j2-mid/complete"
  auth = f"Bearer {ai21key}"

  payload = {
    "numResults": 1,
    "maxTokens": 25,
    "minTokens": 0,
    "temperature": 0.7,
    "topP": 1,
    "topKReturn": 0,
    "frequencyPenalty": {
      "scale": 0,
      "applyToWhitespaces": True,
      "applyToPunctuations": True,
      "applyToNumbers": True,
      "applyToStopwords": True,
      "applyToEmojis": True
    },
    "presencePenalty": {
      "scale": 0,
      "applyToWhitespaces": True,
      "applyToPunctuations": True,
      "applyToNumbers": True,
      "applyToStopwords": True,
      "applyToEmojis": True
    },
    "countPenalty": {
      "scale": 0,
      "applyToWhitespaces": True,
      "applyToPunctuations": True,
      "applyToNumbers": True,
      "applyToStopwords": True,
      "applyToEmojis": True
    },
    "prompt": prompt
  }
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": auth
  }
  response = requests.post(url, json=payload, headers=headers)
  ans = response.json()
  # print(json.dumps(ans, indent=2))
  return ans['completions'][0]['data']['text']

def getSpotifyTrack(summary):
  clientID = os.environ['CLIENT_ID']
  clientSecret = os.environ['CLIENT_SECRET']

  url = "https://accounts.spotify.com/api/token"
  data = {"grant_type":"client_credentials"}
  auth = HTTPBasicAuth(clientID, clientSecret)

  response = requests.post(url, data=data, auth=auth)
  accessToken = response.json()["access_token"]

  #print(response.ok)
  #print(response.json())
  #print(response.status_code)
  summary = summary.replace(",", "")
  summary = summary.replace(" ", "%20")

  url = "https://api.spotify.com/v1/search"
  headers = {'Authorization': f'Bearer {accessToken}'}
  search = f"?q={summary}&type=track&limit=5&offset=0"
  fullURL = f"{url}{search}"

  response = requests.get(fullURL, headers=headers)
  data = response.json()
  # print(json.dumps(response.json(), indent=2))
  track = data['tracks']['items'][0]
  # for track in data["tracks"]["items"]:
  print(track["name"])
  print(track["preview_url"])
  print(track["external_urls"]["spotify"])

getnews(5)
