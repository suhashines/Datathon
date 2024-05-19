from selenium_script import getWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# this code downloads all the data from the following website using a combination of
# selenium and bs4

driver = getWebDriver()


url = 'https://webscraper.io/test-sites/e-commerce/allinone'


driver.get(url)

print(driver.title)

df = pd.DataFrame(columns = ['name','description','price','image','review','rating','category'])

def scrape(driver,category):
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    cards = soup.find_all('div',class_='product-wrapper card-body')
    print(len(cards))

        
    base_link = 'https://webscraper.io'

    
    for i in range(len(cards)):

        image = base_link+cards[i].img.attrs['src']
        price = cards[i].h4.string
        name =  cards[i].a.string
        description = cards[i].p.string

        rating = cards[i].find('div',class_='ratings')
        paragraphs = rating.findAll('p')

        review =  paragraphs[0].string

        rating = paragraphs[1].attrs['data-rating']

        df.loc[len(df)] = [name,description,price,image,review,rating,category]


try:

    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.ID, 'side-menu')))

    sidebar = driver.find_element(By.ID, 'side-menu')

    print(sidebar)

    #sidebar located 

    items = sidebar.find_elements(By.TAG_NAME,'a')

    print(len(items))

    computer_link = items[1]
    cat = computer_link.text

    computer_link.click()

    wait.until(EC.presence_of_element_located((By.ID, 'side-menu')))

    sidebar = driver.find_element(By.ID, 'side-menu')

    #scrap computers
 
    scrape(driver,cat)

    items = sidebar.find_elements(By.TAG_NAME,'a')

    print(len(items))

    for i in range(2,5):
        link = items[i]
        cat = link.text 
        link.click()
        time.sleep(5)
        
        scrape(driver,cat)

        if(i==4):
            sidebar = driver.find_element(By.ID, 'side-menu')
            sub_item = sidebar.find_elements(By.TAG_NAME,'a')
            sub_link = sub_item[3]
            sub_cat = sub_link.text
            sub_link.click()
            time.sleep(5)
            scrape(driver,sub_cat)
            driver.back()
            time.sleep(5)

        driver.back()
        time.sleep(5)



except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
    print(df)

