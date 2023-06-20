import urllib.request
from bs4 import BeautifulSoup
import requests

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"

url = "https://search.aol.com/aol/search?q=555"
headers = {
    "User-Agent": user_agent,
}

request = urllib.request.Request(url, None, headers)  # The assembled request
response = urllib.request.urlopen(request)
data = response.read()  # The data u need

soup = BeautifulSoup(data, "html.parser")

content = soup.find(class_="mb-15 reg searchCenterMiddle")

icontent = content.find(class_="dd bing_dd fst lst Img")


a1 = icontent.find(class_="compText")
pmorepic = a1.text
print(pmorepic + "pppppppppppppppppppppppppppppppppppppppppppppppppp")
a = a1.find("a")
pmorpicaddress = a.get("href")
print(
    pmorpicaddress
    + "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
)
a1.a["href"] = "214214214"
print(a1.a["href"] + "gggggggggggggggggggggggggggggg")


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
        print(d2.get("data-src"))  # >>>>>>>> in the pcontent name is data-src   BUT
        # in page source name is src ??????????????????????????????????
        aol_ppic.append(d2.get("data-src"))

    print("************************************************************")

print(
    "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
)


##########################downloading image#########################
x = 1
for i in aol_ppic:
    print(x)
    if ".svg" in i:
        print(i + "cannot be downloaded")

    else:
        try:
            print(i)
            r = requests.get(i).content

            print(r)
            filename = "aol/image" + str(x) + ".jpg"
            with open(filename, "wb+") as f:
                f.write(r)
        except:
            pass
    x = x + 1

    # downloading image
