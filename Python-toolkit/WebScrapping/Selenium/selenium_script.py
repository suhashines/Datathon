from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Path to the ChromeDriver executable
path = "C:\\Program Files (x86)\\chromedriver.exe"


def getWebDriver():


    # Create a service object
    service = Service(executable_path=path)

    # Create a ChromeOptions object
    options = Options()

    # Initialize the WebDriver with the service and options
    driver = webdriver.Chrome(service=service, options=options)

    return driver
