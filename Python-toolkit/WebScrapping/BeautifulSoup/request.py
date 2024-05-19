import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'

r = requests.get(url)

# print(r.status_code) -> 200-300 -> ok , 400-500 -> client error , 500+ ->server error

soup = BeautifulSoup(r.text,"lxml")
#print(soup)

# to only get the first div

# print(soup.div)

# finding first list inside div
# print(soup.div.li)

#finding attributes

# div = soup.div
# div_attrs = div.attrs 

# print(div_attrs['class'])


# finding navigable strings

# print(soup.div.p.string)
# print(soup.header.div.span.string)


# using find function

# title = soup.find('a',{'title':'Acer Aspire ES1-572 Black'}).string
# print(title)

# price = soup.find('h4',{'class':'price float-end card-title pull-right'}).string
# print(f'price: {price}')

# desc = soup.find('p',{'class':'description card-text'}).string
# # desc = soup.find('p',class_ = 'description card-text').string
# print(f'description: {desc}')


cards = soup.findAll('div',class_ = 'product-wrapper card-body')

base_link = 'https://webscraper.io'

df = pd.DataFrame(columns = ['name','description','price','image','review','rating'])


for i in range(len(cards)):

    image = base_link+cards[i].img.attrs['src']
    price = cards[i].h4.string
    name =  cards[i].a.string
    description = cards[i].p.string

    rating = cards[i].find('div',class_='ratings')
    paragraphs = rating.findAll('p')

    review =  paragraphs[0].string

    rating = paragraphs[1].attrs['data-rating']

    df.loc[len(df)] = [name,description,price,image,review,rating]


print(df)

df.to_csv('products.csv',index=False)


