from bs4 import BeautifulSoup
  
def parse(html):
  soup = BeautifulSoup(data, 'lxml')
  reviews = soup.findAll('div', { 'itemprop': 'review' })

  for review in reviews:
    author = review.find('meta', { 'itemprop': 'author' })['content']
    description = review.find('meta', { 'itemprop': 'description' })['content']
    rating = review.find('meta', { 'itemprop': 'ratingValue' })['content']
    datePublished = review.find('meta', { 'itemprop': 'datePublished' })['content']
    
    print(author, description, rating, datePublished)

file = open('market.html', 'r', encoding='utf-8')
data = file.read()
file.close()

parse(data)