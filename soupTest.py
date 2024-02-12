from bs4 import BeautifulSoup
import requests

url = 'https://www.nba.com/stats/players/advanced'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())