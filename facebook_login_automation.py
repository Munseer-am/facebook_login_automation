from time import sleep
import hashlib
from selenium import webdriver


p = '8e00596ad8de2213ff8f8d8478d5362c'

i = str(input("Enter password: "))
enc = hashlib.md5(i.encode()).hexdigest()
if p != enc:
    quit()
else:

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
