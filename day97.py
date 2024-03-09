import requests, os
from bs4 import BeautifulSoup
#import openai

url = "https://en.wikipedia.org/wiki/Cancer"
#https://en.wikipedia.org/wiki/Karl_M%C3%B6%C3%B6l

#url = input("Paste wikipedia url: ")
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

#print(html)


# mw-headline 0
# mw-body-content 1
# mw-content-subtitle 0
# mw-content-text 0
# mw-headline 51
# div toclimit-3
# mw-content-ltr 1 147
# mw-parser-output

text = ""

article = soup.find_all("div",{"class":"mw-content-ltr"})[0] ## FUNCIONA

#article = soup.find_all("div",{"class":"mw-parser-output"})[1]
#print(len(article))

content = article.find_all("p")
for articles in article:
  for p in content:
    text += p.text
#print(text)
print(len(content))

# TODO - Send this text to openAI for summary in 3 paragraphs.

#openai.organisation = os.environ['organisationID']
#openai.api_key = os.environ['openai']
#openai.Model.list()

#prompt = f"""Summarize the text below in no more than 3 paragraphs. {text}"""

#response = openai.Completion.create(model="text-davinci-002", prompt=text, temperature=0, max_tokens=5)

refs = soup.find_all("ol",{"class":"references"})
for ref in refs:
  print(ref.text.replace("^ ",""))

#print(response["choices"][0]["text"].strip())
