import requests
from bs4 import BeautifulSoup
import pandas as pd


# access any website using the user agent of your browser. To find what your user agent is, simply
# search whatismybrowser.com -> my browser settings -> user-agent

url = 'https://www.amazon.com/b?node=283155' 
user_agent = 'https://explore.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes'

headers = ({'User-Agent': user_agent, 'Accept-Language':'en-US,en;q=0.5'})

r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.text,'lxml')

holder = soup.find('div',class_='p13n-gridRow _cDEzb_grid-row_3VsqC')

cards = holder.find_all('div',id='gridItemRoot')

print(len(cards))


# let's try to find everything for this card


df = pd.DataFrame(columns=['name','image','stars','downloads','price'])


for i in range(0,len(cards)):


    #name

    name = cards[i].find('span',class_='a-size-small').div.string

    #stars

    stars = cards[i].find('span',class_='a-icon-alt').string
  

    #downloads

    downloads = cards[i].findAll('span',class_='a-size-small')[1].string
   

    price = cards[i].find('span',class_='a-size-base a-color-price').span.string

   

    image = cards[i].find('img').attrs['src']
   

    df.loc[len(df)] = [name,image,stars,downloads,price]

#unfortunately,beautiful soup cannot work with javascript,we need selenium for that

print(len(df))