import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

URL = "http://kq.neusoft.com/"

browser=webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.get(URL)
time.sleep(3)

browser.quit()
