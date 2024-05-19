import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.timesjobs.com/jobfunction/it-software-jobs'

r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')

print(soup)

