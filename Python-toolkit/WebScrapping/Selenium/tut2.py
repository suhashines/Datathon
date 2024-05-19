from selenium_script import getWebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

driver = getWebDriver()

url = 'https://www.timesjobs.com/jobfunction/it-software-jobs'


driver.get(url)

print(driver.title)
#it is working 


# id,name,class hierarchy to maintain 


try:

    wait = WebDriverWait(driver,10)

    search = wait.until(EC.presence_of_element_located((By.ID, 'txtKeywords')))

    print(search.get_attribute('class'))

    search.send_keys('software developer')

    search.send_keys(Keys.RETURN)

    name = driver.find_element(By.CLASS_NAME,'joblist-comp-name')

    print(name.text)

    # button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'a')))
    # button.click()

    pages = driver.find_elements(By.TAG_NAME,'em')

    page_2 = pages[1]

    page_2_btn = page_2.find_element(By.TAG_NAME,'a')

    print(page_2_btn)



except Exception as e:
    print("Error:", e)

finally:
    driver.quit()

