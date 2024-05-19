from selenium_script import getWebDriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#it searches elephant on google

driver = getWebDriver()

url = "https://www.google.com"

driver.get(url)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,'textarea')))

search = driver.find_element(By.TAG_NAME,'textarea')

search.clear()

search.send_keys("elephant"+Keys.ENTER)

time.sleep(5)

# now we want to click to a link that says Elephant

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Elephant")

link.click()

time.sleep(5)

driver.quit()