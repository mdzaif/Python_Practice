#!/usr/bin python3

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

user = input("Enter your GitHub user name: ").strip()
# link contains the a user's github repositories list link.
link = 'https://github.com/'+user+'?tab=repositories'
r = requests.get(link)
rc = r.content
s = BeautifulSoup(rc, 'html.parser') # prasering with html type of the content from the request.
q = s.find_all('li', {'class' : 'col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source'})

li = []
for repo in q:
    dct = {}
    dct['Repository Name'] = repo.find('a', {'itemprop' : 'name codeRepository'}).text.strip()
    if(repo.find('span', {'itemprop' : 'programmingLanguage'})):
        dct['Programming Language'] = repo.find('span', {'itemprop' : 'programmingLanguage'}).text.strip()
    else:
        dct['Programming Language'] = "No Programming Language Found"
    if(repo.find('p', {'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'})):
        dct['Description'] = repo.find('p', {'class': 'col-9 d-inline-block color-fg-muted mb-2 pr-4'}).text.strip()
    else:
        dct['Description'] = "No Description Found"
    dct['Last Update'] = repo.find('relative-time', {'class' : 'no-wrap'}).text.strip()
    if(repo.find('a', {'class': 'Link--muted mr-3'})):
        dct['Total Star'] = repo.find('a', {'class': 'Link--muted mr-3'}).text.strip()
    else:
        dct['Total Star'] = '0'
    ht = repo.find('a')
    ht = ht.get('href')
    ht = 'https://github.com'+ht
    dct['Repository Link'] = ht
    li.append(dct)
df = pd.DataFrame(li)
df.to_csv('list_of_project.csv')
print("process completed!")
   
