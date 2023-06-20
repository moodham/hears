def fun():
    fun.a = 15


fun()
n = fun.a
print(n)


#
# aol web
import requests

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0"

url = "https://search.aol.com/aol/search?q=م"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


response = requests.get(url, headers=headers)



data = response.content  # The data u need
print (data)