from time import sleep
from selenium import webdriver


browser = webdriver.Chrome('c:/python/chromedriver.exe')

browser.get('https://facebook.com')

sleep(2)
user = browser.find_element_by_id('email')
#user.click()

user.send_keys('Your Email Here')

pas = browser.find_element_by_xpath('//*[@id="pass"]')
#pas.click()

pas.send_keys('Your Password Here')

sleep(2)

button = browser.find_element_by_name('login')
button.click()

search = browser.find_element_by_xpath('//*[@id="mount_0_0_JI"]')
search.click()
search.send_keys('Mujeeb Arangath')
