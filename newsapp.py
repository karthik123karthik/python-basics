import requests

query = input("enter the topic you are intrested in ? - ")
url = (f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey=cb0d4b5127684eba973a8937d135ef28")
response = requests.get(url)
data = response.json()
news = data["articles"]
for article in news:
    print(article["title"])
    print("---------------------------------------------")
    print(article["description"])
    print("----------read more---------")
    print(article["url"])
    print("-----------------------------------------------")
    print("-----------------------------------------------")
