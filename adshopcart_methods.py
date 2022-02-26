import datetime
import adshopcart_locators as locators
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    #  print test start day and time
    print(f'Test started at: {datetime.datetime.now()}')

    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser respond in general
    driver.implicitly_wait(30)

    # navigating to Moodle app website
    driver.get(locators.advantage_shopping_cart_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.advantage_shopping_cart_url and driver.title == "\u00A0""Advantage Shopping":
        print(f' we are at advantage online shopping homepage --{driver.current_url}')
        print(f'we\'re seeing title message --{driver.title} ')

    else:
        print(f'we\'re not at the advantage online shopping homepage, Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()



