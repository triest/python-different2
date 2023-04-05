from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
opts.add_experimental_option("prefs", prefs)


# enter complete path of chrome driver as argument to below line of code
browser = webdriver.Chrome('C:\\Users\\BLR153\\AppData\\Local\\Programs\\Python\\Python36-32\\selenium\\chromedriver.exe')
# browser = webdriver.Firefox()

browser.get('http://www.google.com')

time.sleep(10)

browser.quit()