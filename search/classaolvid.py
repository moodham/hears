# aol web
import requests
from bs4 import BeautifulSoup
from .models import inspect


user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"

url = "https://search.aol.com/aol/video;_ylt=AwrNPpqqTmZk9kgImDtnCWVH;_ylu=c2VjA3NlYXJjaAR2dGlkAw--?q="
headers = {
    "User-Agent": user_agent,
}


class findaolvid:
    def __init__(self, ADDR):
        self.ADDR = ADDR

        entery = inspect.objects.filter(author_ip= ADDR).order_by("-date") # last date

        self.n = entery.values()[0]["searchitems"]


    def ww(self):
        aol_ww = []

        response = requests.get(url + self.n , headers=headers)
        print(response)
              
          # The assembled request
        
        data = response.content  # The data u need
        
        soup = BeautifulSoup(data, "html.parser")

        aol_wv=[]
        try :

            contentre = soup.find(class_="results clearfix")
            
            contentre = contentre.find_all("li",class_="vr vres")
            

            print(
                "yyyyyyyyyyyyyyyyggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
            )
            for i in contentre:
                print(i)
                lis = []
                d = i.find("a")
                if hasattr(d, "data-rurl"):
                    print(d.get("data-rurl"))
                    
                    # Relatedsearches.append(d.get("href"))
                    
                    lis.append(d.get("data-rurl"))

                d = i.find("img")
                if hasattr(d, "src"):
                    print(d)
                    print(d.get("src"),"src")
                
             
                    lis.append(d.get("src"))
                    
                d = i.find("h3")
                if hasattr(d, "text"):
                    
  
                    lis.append(d.text)

                d = i.find(class_="v-age")
                if hasattr(d, "text"):
                    
                    
                    lis.append(d.text)

                d = i.find(class_="url")
                if hasattr(d, "text"):
                    
                    
                    lis.append(d.text)
                    

                print("********************************************wpic*******")
                aol_wv.append(lis)
        except:
            pass
        

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        #print(aol_wv)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

            
        return aol_wv