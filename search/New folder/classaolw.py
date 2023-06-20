# aol web
import urllib.request
from bs4 import BeautifulSoup


user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"

url = "https://search.aol.com/aol/search?q="
headers = {
    "User-Agent": user_agent,
}


class findaol:
    def __init__(self, name):
        self.name = name

    def ww(self):
        aol_ww = []

        request = urllib.request.Request(
            url + self.name, None, headers
        )  # The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()  # The data u need

        soup = BeautifulSoup(data, "html.parser")

        x = 0
        content = soup.find(class_="mb-15 reg searchCenterMiddle")
        # print (content)
        # content2 = content.find('a')
        # print (content2)
        wcontent = content.find_all(class_="algo-sr")

        # print (wcontent)
        for i in wcontent:
            x = x + 1
            lis = []
            if x > 1:
                print(
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                    x,
                )
                # print(i)

                d = i.find("a")
                # print(d)
                if hasattr(d, "text"):
                    lis.append(d.text)
                    print(d.text)

                d2 = i.find("p")
                if hasattr(d2, "text"):
                    print(d2.text)
                    lis.append(d2.text)

                d3 = i.find("span", class_="fz-ms fw-m fc-12th wr-bw lh-17")
                if hasattr(d3, "text"):
                    print(d3.text)
                    lis.append(d3.text)
                print("****************************************ww********************")
                aol_ww.append(lis)
        return aol_ww

    def wrs(self):
        aol_wrs = []
        request = urllib.request.Request(
            url + self.name, None, headers
        )  # The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()  # The data u need

        soup = BeautifulSoup(data, "html.parser")

        contentre = soup.find(class_="compTable m-0 ac-1st td-n fz-ms")
        contentre = contentre.find_all("tr")

        print(
            "yyyyyyyyyyyyyyyyggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
        )
        for i in contentre:
            # print(i)
            lis = []
            d = i.find("a")
            if hasattr(d, "href"):
                print(d.get("href"))
                print(d.text)
                # Relatedsearches.append(d.get("href"))
                lis.append(d.text)
                lis.append(d.get("href"))

                aol_wrs.append(lis)
            print("********************************************wrs*******")
        return aol_wrs

    def wpn(self):
        aol_wpn = []
        request = urllib.request.Request(
            url + self.name, None, headers
        )  # The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()  # The data u need

        soup = BeautifulSoup(data, "html.parser")

        contentp = soup.find(class_="pages")
        contentp = contentp.find_all("a")

        for i in contentp:
            # print(i)

            if hasattr(i, "href"):
                print(i.get("href"))
                aol_wpn.append(i.get("href"))

        print("***********************************************************wgn*")
        return aol_wpn

    def wp(self):
        aol_wp = []

        try:
            request = urllib.request.Request(
                url + self.name, None, headers
            )  # The assembled request
            response = urllib.request.urlopen(request)
            data = response.read()  # The data u need

            soup = BeautifulSoup(data, "html.parser")

            content = soup.find(class_="mb-15 reg searchCenterMiddle")
            
            icontent = content.find(class_="dd bing_dd fst lst Img")

            a1 = icontent.find(class_="compText")
            pmorepic = a1.text
            print(pmorepic + "pppppppppppppppppppppppppppppppppppppppppppppppppp")
            
            if a1.find("a"):
                a = a1.find("a")
                print(a.get("href"))
                
                pmorpicaddress = a.get("href")
            else:
                pass

            aol_palt = []
            aol_ppic = []

            pcontent = icontent.find_all("li")
            print(pcontent)
            for i in pcontent:
                # print(i)

                d2 = i.find("img")
                if hasattr(d2, "alt"):
                    print(d2["alt"])
                    aol_palt.append(d2["alt"])
                    print(
                        d2.get("data-src")
                    )  # >>>>>>>> in the pcontent name is data-src   BUT
                    # in page source name is src ??????????????????????????????????
                    aol_ppic.append(d2.get("data-src"))
                    aol_wp.append((d2["alt"], d2.get("data-src")))

                print("************************************************************")
            aol_wp.append(pmorpicaddress)
            print(aol_wp)
            print(
                "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            )

            return aol_wp
        except:
            pass


    def wv(self):
        aol_wv = []
        print ("wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...wv...")

        try:
            request=urllib.request.Request(url+ self.name,None,headers) #The assembled request
            response = urllib.request.urlopen(request)
            data = response.read() # The data u need

            soup = BeautifulSoup(data, 'html.parser')

            content = soup.find(class_="mb-15 reg searchCenterMiddle")

            icontent = content.find(class_="dd Video")
            print( "################################################")

            a1=icontent.find(class_="compText")
            vmorevideo=a1.text
            print (vmorevideo+"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
            a=a1.find("a")
            global vmorvideoaddress
            vmorvideoaddress =a.get('href')
            


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
                aol_wv.append((d.text,d2.text,d3.text,d4.get('src')))
                print("************************************************************")
            print ("aol_wvaol_wvaol_wvaol_wvaol_wvaol_wvaol_wv",aol_wv)
            aol_wv.append(vmorvideoaddress)
            return aol_wv
            

        except:
            print( "exceptexceptexceptexceptexceptexceptexceptexceptexceptexcept")