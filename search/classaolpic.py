# aol web
import requests
from bs4 import BeautifulSoup
from .models import inspect

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"

url = "https://search.aol.com/aol/image;_ylt=AwrFYFKB32RkKbMNEAdpCWVH;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?q="
headers = {
    "User-Agent": user_agent,
}


class findaolpic:
    def __init__(self, ADDR):
        self.ADDR = ADDR

        entery = inspect.objects.filter(author_ip= ADDR).order_by("-date") # last date

        self.n = entery.values()[0]["searchitems"]

        
    
    
    def ww(self):
        

        response = requests.get(url + self.n , headers=headers)
        print(response)
              
          # The assembled request
        
        data = response.content  # The data u need
        
        soup = BeautifulSoup(data, "html.parser")

        aol_wp=[]
        try :

            contentre = soup.find(class_="sres-cntr")
            
            contentre = contentre.find_all("li",class_="ld")
            

            print(
                "yyyyyyyyyyyyyyyyggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
            )
            for i in contentre:
                print(i)
                lis = []
                d = i.find("a")
                if hasattr(d, "href"):
                    print(d.get("href"))
                    
                    # Relatedsearches.append(d.get("href"))
                    
                    lis.append(d.get("href"))

                d = i.find("img")
                if hasattr(d, "data-src"):
                    print(d.get("data-src"),"data-src")
                    
                    
                    
                    lis.append(d.get("data-src"))
                    lis.append(d.get("style"))

                print("********************************************wpic*******")
                aol_wp.append(lis)
        except:
            pass
        

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(aol_wp)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

            
        return aol_wp