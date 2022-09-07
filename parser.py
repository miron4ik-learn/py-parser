import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
  
def parse(html):
  soup = BeautifulSoup(data, 'lxml')
  vacancies = soup.findAll('div', { 'class': 'job-link' })
  
  results = {
    'href': [],
    'title': [],
    'description': [],
    'info': [],
  }
  
  for vacancy in vacancies:
    href = vacancy.find('a')['href']
    title = vacancy.h2.text.strip()
    description = vacancy.p.text.strip()
    info = vacancy.b.text.strip()
    
    results['href'].append('https://www.work.ua' + href)
    results['title'].append(title)
    results['description'].append(description)
    results['info'].append(info)
    
  return results

start_page = 1
max_page = 1
  
result_list = {
  'href': [],
  'title': [],
  'description': [],
  'info': [],
}

for page in range(start_page, max_page + 1):
  url = 'https://www.work.ua/ru/jobs-kyiv/?page=' + str(page)
  
  response = requests.get(url)
  response.encoding = 'utf-8'

  data = response.text
  result = parse(data)
  
  for h in result['href']:
    result_list['href'].append(h)
  for t in result['title']:
    result_list['title'].append(t)
  for d in result['description']:
    result_list['description'].append(d)
  for i in result['info']:
    result_list['info'].append(i)
  
  # time.sleep(10)
  
FILE_NAME = 'data.csv'
  
df = pd.DataFrame(data=result_list)
df.to_csv(FILE_NAME)