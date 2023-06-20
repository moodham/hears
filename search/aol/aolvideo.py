import urllib.request
from bs4 import BeautifulSoup
import requests
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'

url = 'https://search.aol.com/aol/search?q=66'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need

soup = BeautifulSoup(data, 'html.parser')

content = soup.find(class_="mb-15 reg searchCenterMiddle")

icontent = content.find(class_="dd Video")


a1=icontent.find(class_="compText")
vmorevideo=a1.text
print (vmorevideo+"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
a=a1.find("a")
vmorvideoaddress =a.get('href')
print (vmorvideoaddress+"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")



aol_vtitle=[]
aol_vsitename=[]
aol_vaddress=[]
aol_vpic=[]

vcontent = icontent.find_all("li")

for i in vcontent:

    #print(i)
    
    d= i.find('a')
    #print(d)
    aol_vaddress.append(d.text)
    print(d.text)

    d2 =i.find(class_="mt-8")
    if hasattr(d2, "text"):

        print(d2.text)
        aol_vtitle.append(d2.text)

    d3 = i .find('span',class_="cite fc-2nd fs-100 tc d-b mr-24")
    if hasattr(d3, "text"):
        print(d3.text)
        aol_vsitename.append(d3.text)

    d4 = i .find(class_="s-img d-b")
    if hasattr(d4, "img"):

        print(d4.get('src'))
        aol_vpic.append(d4.get('src'))
    print("************************************************************")

print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


#downloading image
x=1
for i in aol_vpic:
    
    print(x)
    if '.svg' in i:
        print(i  + "cannot be downloaded")

    else:
        try:

        
            print(i)
            r=requests.get(i).content
            
            print(r)
            filename='aol/image'+str(x)+'.jpg'
            with open(filename,'wb+') as f:
                f.write(r)
        except:
            pass
    x=x+1



    #downloading image


































