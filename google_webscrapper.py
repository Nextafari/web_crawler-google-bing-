from bs4 import BeautifulSoup
import requests

search = input("Begin search: ")    #create a search input
url = "https://google.com/search?"  #create url variable for the website being crawled
params = {"q": search}  #parameters for inserting the search into the get method
#mimicks the request to look like it's coming from a browser
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
headers = {"user-agent": USER_AGENT}    #mimicks a client's request from a browser and prevents being blocked off webscrapping
r = requests.get(url, params=params, headers=headers)   #request (.get) method

soup = BeautifulSoup(r.content, "html.parser")  #the first argument is the content from the get request, and "html.parser" 
results = soup.find("div", {"id": "search"})    #variable for html element housing search results with values (html tags/id/class) passed as args of ("strings, and dict")
links = results.find_all("div", {"class": "r"}) #variable for html tag housing the content(weblinks, news, etc) with attributes of the html elements as arguments of ("strings, and dict")


#A function to crawl the web results from google

def google_webcrawler():
    #looping through the results of the variable links
    for i in links:     
        news_title = i.find("a").text #a variable for holding and converting to text from links above
        news_link = i.find('a').attrs["href"] #a variable for holding the weblink gotten from "links" above

        if news_title and news_link:        #conditional for printing_news title and news_link
           print(news_title)
           print(news_link)       
google_webcrawler()