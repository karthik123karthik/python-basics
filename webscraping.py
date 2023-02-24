import requests
from bs4 import BeautifulSoup

response  = requests.get("https://google.com/")
soup = BeautifulSoup(response.text, "html5lib")

table = soup.find('div', attrs={'class':'gbh'})
print(table.prettify())
