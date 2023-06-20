#aol web
import urllib.request
from bs4 import BeautifulSoup
user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'

url = 'https://search.aol.com/aol/search?q=555'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need


#print (data)
print ("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")

data1 = str(data.decode('UTF-8'))

print (type(data1))

#print (data1)
f = open("myfile.html", "w", encoding="utf-8")

f.write(data1)
f.close()

soup = BeautifulSoup(data, 'html.parser')

x=0
content = soup.find(class_="mb-15 reg searchCenterMiddle")
#print (content)
#content2 = content.find('a')
#print (content2)
wcontent = content.find_all(class_="algo-sr")

#print (wcontent)

aol_wtitle=[]
aol_wdesc=[]
aol_waddress=[]

for i in wcontent:
    x=x+1

    if x>1:
        print(x,x,x,x,x,x,x,x,)
        #print(i)
        
        d= i.find('a')
        #print(d)
        aol_wtitle.append(d.text)
        print(d.text)

        d2 =i.find("p")
        if hasattr(d2, "text"):

            print(d2.text)
            aol_wdesc.append(d2.text)

        d3 = i .find('span',class_="fz-ms fw-m fc-12th wr-bw lh-17")
        if hasattr(d3, "text"):
            print(d3.text)
            aol_waddress.append(d3.text)
        print("************************************************************")

print(aol_wtitle,aol_wdesc,aol_waddress)



##########################down page number#########################
contentp = soup.find(class_="pages")
contentp = contentp.find_all("a")
pagenumber = []

for i in contentp:

    #print(i)
    
    
    if hasattr(i, "href"):

        print(i.get("href"))
        pagenumber.append(i.get("href"))


    print("************************************************************")


#################    Related searches #########################



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






