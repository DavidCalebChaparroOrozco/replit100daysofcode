# # API NEWS
# import requests, json, os

# newsKey = os.environ['newsapi']
# country = "us"

# url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsKey}"

# result = requests.get(url)
# data = result.json()
# #print(json.dumps(data, indent=2))

# for article in data['articles']:
#   print(article['title'])
#   print(article['url'])
#   print(article['content'])



# # Open AI
# import openai

# openai.organization = os.environ['organizationID']
# openai.api_key = os.environ['openai']
# openai.Model.list()

# prompt = "Give me 100 days of project ideas using Python that work for my portfolio. Topics related to AI, Flask and Tkinter."

# response = openai.Completion.create(model="text-davinci-002",
#                                     prompt=prompt,
#                                     temperature=0,
#                                     max_tokens=6)
# print(response["choices"][0]["text"].strip())






import requests, json, os, openai

news = os.environ['newsapi']
openai.organisation = os.environ['organizationID']
openai.api_key = os.environ['openai']
openai.Model.list()

country = "us"
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"

result = requests.get(url)
data = result.json()
#print(json.dumps(data, indent=2))

counter = 0
for article in data["articles"]:
  counter +=1
  if counter > 5:
    break
  #print(f"""Summararise{article["url"]} in one sentence.""")
  prompt = (f"""Summararise{article["url"]} in one sentence.""")
  response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)
  print(response["choices"][0]["text"].strip())

