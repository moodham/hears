#aol web
import urllib.request
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'

url = 'http://www.parseek.ir/search/?qu=555'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need


#print (data)

soup = BeautifulSoup(data, 'html.parser')

x=0
content = soup.find("div",id="wrapper")
#print (content)
#content2 = content.find('a')
#print (content2)
wcontent = content.find_all(class_="re")

#print (wcontent)

aol_wtitle=[]
aol_wdesc=[]
aol_waddress=[]

x=0
for i in wcontent:
    x=x+1

    if x>0:
        print(x,x,x,x,x,x,x,x,)
        #print(i)
        
        d= i.find('a')
        #print(d)
        aol_wtitle.append(d.text)
        print(d.text)
        print(d.get('href'))
        aol_waddress.append(d.get('href'))

        d2 =i.find(class_="d")
        if hasattr(d2, "text"):

            print(d2.text)
            aol_wdesc.append(d2.text)



        print("************************************************************")

print(aol_wtitle,aol_wdesc,aol_waddress)

