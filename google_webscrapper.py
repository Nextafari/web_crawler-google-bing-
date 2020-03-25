from bs4 import BeautifulSoup
import requests

search = input("Begin search: ")    #create a search input
url = "https://google.com/search?"  #create url variable for the website being crawled
params = {"q": search}  #parameters for inserting the search into the get method
#mimicks the request to look like it's coming from a browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
headers = {"user-agent": USER_AGENT}    #mimicks a client's request from a browser and prevents being blocked off webscrapping
r = requests.get(url, params=params, headers=headers)   #request (.get) method

soup = BeautifulSoup(r.content, "html.parser")  #
results = soup.find("div", {"id": "search"})
links = results.find_all("div", {"class": "r"})



def google_webcrawler():
    for i in links:
        news_title = i.find("a").text
        news_link = i.find('a').attrs["href"]

        if news_title and news_link:
           print(news_title)
           print(news_link)       
google_webcrawler()