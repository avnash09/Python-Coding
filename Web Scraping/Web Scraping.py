import requests

response = requests.get('https://www.example.com/')

#print(response.text)

import bs4

soup = bs4.BeautifulSoup(response.text, 'lxml')

print(soup)

soup.select('title') #returns a list
print(f"soup.select('title'): {soup.select('title')}")

page_title = soup.select('title')[0].getText()

print(f"soup.select('title')[0].getText(): {page_title}")