#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

URL = "https://www.rosmm8.com"
count = 1

try:
    browser=webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    browser.get(URL)
    print browser.page_source
    # time.sleep(3)
except Exception as e:
    print e
    browser.quit()
    raise e


