from bs4 import BeautifulSoup
import requests

url = 'https://nuforc.org/ndx/?id=event'

r = requests.get(url)

soup = BeautifulSoup(r.content, features="html.parser")

date_links = []
full_url = []

for row in soup.find_all('a', href=True):
    if row['href'].startswith('/subndx/?id='):
        date_links.append(row['href'])

print(date_links)

for date_link in date_links:
    date_url = 'https://nuforc.org' + date_link
    full_url.append(date_url)
    
print(full_url)
