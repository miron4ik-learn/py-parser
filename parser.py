import time
import requests
from bs4 import BeautifulSoup
  
def parse(html):
  soup = BeautifulSoup(data, 'lxml')
  vacancies = soup.findAll('div', { 'class': 'job-link' })
  
  for vacancy in vacancies:
    href = vacancy.find('a')['href']
    title = vacancy.h2.text.strip()
    description = vacancy.p.text.strip()
    info = vacancy.b.text.strip()
    
    print('Ссылка', href, sep=': ')
    print('Название', title, sep=': ')
    print('Описание', description, sep=': ')
    print('Информация', info, sep=': ')
    print()

start_page = 1
max_page = 5

for page in range(start_page, max_page + 1):
  url = 'https://www.work.ua/ru/jobs-kyiv/?page=' + str(page)
  
  response = requests.get(url)
  response.encoding = 'utf-8'

  data = response.text
  parse(data)
  
  time.sleep(10)