from bs4 import BeautifulSoup
import requests 

search = input("Enter your search here: ")
params = {"q": search}
url = ("https://www.bing.com/search")
USER_AGENT ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
headers = {"user-agent": USER_AGENT}
#create a variable for the requests
r = requests.get(url, params=params, headers=headers)

def bing_webcrawler():
    soup = BeautifulSoup(r.text, "html.parser")  #content of the request(variable r)
    results = soup.find("ol", {"id": "b_results"})  #this must be a dictionary
    links = results.find_all("li", {"class": "b_algo"}) #this must be a dictionary

    for i in links:
        #Variables for the information we want to get from the links
        item_text = i.find("a").text
        item_link = i.find("a").attrs["href"]
        if item_text and item_link:
            print(item_text)
            print(item_link)
        
bing_webcrawler()
        
        





#Steps to make a webcrawler using BeautifulSoup

#1)Import BeautifulSoup from bs4, also import requests
#2)create a search variable to contain an input to be searched for
#3)create a parameter to contain the following arguments on line 5 above to send the (get_request) 
#variable of q, equal to what we search for along the line. this basicially tells the url to append "q" and the search keyword 
#4)create a requests variable with a .get request and pass in the website you want to crawl and you pass in params
#5)create a variable like the one on line 8, and assign a value to parse the html document and return it as a text
#6)create a variable results and pass in the html element you are looking to get info and also the attributes you are looking for
# (more like get the  element with the whole search result and the id or other class there) as seen in line 9

#7)create another variable called links that will search the "result" to return what you need from inside the tag housing 
#the various elements you want information from eg all the elements in a container
#8)We use a for loop to loop through the data gotten from the "links" variable above and we put the values in variables
#
#