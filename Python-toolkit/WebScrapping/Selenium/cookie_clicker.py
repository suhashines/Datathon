from selenium_script import getWebDriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = getWebDriver()

url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)

time.sleep(2)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"langSelect-EN")))

language = driver.find_element(By.ID,"langSelect-EN")

language.click()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"bigCookie")))

button = driver.find_element(By.ID,"bigCookie")

cookies = 0 

product_prefix = "product"
product_price_prefix = "productPrice"

while True:

    button.click()

    cookie_text = driver.find_element(By.ID,"cookies").text

    cookies = int(cookie_text.split()[0])

    for i in range(4):

        # WebDriverWait(driver,5).until(EC.presence_of_element_located(By.ID,"productPrice"+str(i)))

        price_id = product_price_prefix + str(i)
        product_id = product_prefix+str(i)

        print(f"price_id = {price_id}")
        print(f"product_id = {product_id}")


        upgrade_price = int(driver.find_element(By.ID,"productPrice0").text)

        if(cookies>upgrade_price):

            upgrade_button = driver.find_element(By.ID,"product0")
            upgrade_button.click()
            break


time.sleep(5)

driver.quit()