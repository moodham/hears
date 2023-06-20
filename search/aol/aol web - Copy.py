#aol web
import urllib.request
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'

url = 'https://search.aol.com/aol/search?q=566'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need

soup = BeautifulSoup(data, 'html.parser')




contentre = soup.find(class_="compTable m-0 ac-1st td-n fz-ms")
contentre = contentre.find_all("tr")
Relatedsearches = {}
print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in contentre:

    #print(i)
    
    d= i.find("a")
    if hasattr(d, "href"):

        print(d.get("href"))
        print(d.text)
        #Relatedsearches.append(d.get("href"))
        Relatedsearches[d.text] =d.get("href")



    print("************************************************************")

print (Relatedsearches)






