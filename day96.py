import requests
from bs4 import BeautifulSoup

# url = "https://www.yelp.co.uk/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA%2C+United+States"

# response = requests.get(url)
# html = response.text

# #print(html)
# soup = BeautifulSoup(html, 'html.parser')

# myLinks = soup.find_all("a", {"class": "css-1m051bw"})
# print(len(myLinks))

# counter = 0
# for link in myLinks:
#   if counter > 1:
#     print(link.text)
#     print(f"""https://www.yelp.com{link["href"]}""")
#   counter += 1









url = "https://news.ycombinator.com/"

response = requests.get(url)
html = response.text

#print(html)

soup = BeautifulSoup(html, 'html.parser')


# <span class="titleline"><a href="https://github.com/bruhbruhroblox/wallstreetlocal">Show HN: Wallstreetlocal – View investments from America's biggest companies</a><span class="sitebit comhead"> (<a href="from?site=github.com/bruhbruhroblox"><span class="sitestr">github.com/bruhbruhroblox</span></a>)</span></span>

myLinks = soup.find_all("span",{"class": "titleline"})

#print(len(myLinks))
things = ["replit", "python", "apple", "microsoft"]

for link in myLinks:
  text = link.text
  textList = text.split()
  containsWord = False
  for word in textList:
    if word.lower() in things:
      containsWord = True
  if containsWord:
    print(link.text)
    myLink = link.find_all("a")
    print(myLink[0]["href"])
