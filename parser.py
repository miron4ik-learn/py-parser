from bs4 import BeautifulSoup

file = open('for_parsing.html', 'r', encoding='utf-8')
data = file.read()
file.close()

soup = BeautifulSoup(data, 'lxml')

reviews = soup.findAll('div', { 'class': 'review' })

for review in reviews:
  name = review.find('div', { 'class': 'name' }).text.strip()
  comment = review.find('div', { 'class': 'comment' }).text.strip()
  print(name, comment, sep=': ')