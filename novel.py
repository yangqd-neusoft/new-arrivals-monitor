#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# URL = open("info.txt", "r").read()
# count = 1

# try:
#     browser=webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#     browser.get(URL)
#     print "get URL success"
#     time.sleep(3)
# except Exception as e:
#     print e
#     browser.quit()
#     raise e

# nextLink = URL

def getNovel():
    while True:
        URL = open("info.txt", "r").read()
        try:
            browser = webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
            browser.get(URL)

            print "get %s success" % URL

            # time.sleep(5)

            # element_chapter = browser.find_element_by_tag_name("h1")
            element_chapter = browser.find_element_by_id("chapers_biaoti")
            print element_chapter.text
            # browser.quit()
            # break
            # str_chapter = element_chapter.text
            fo = open("novel.txt", "a")
            fo.write(element_chapter.text + '\n\n')
            fo.close()

            element_content = browser.find_element_by_id("chapter_content")
            # str_content = element_content.text
            fo = open("novel.txt", "a")
            fo.write(element_content.text + '\n\n\n')
            fo.close()
            # print "%s complete!" %str(count)
            # count = count + 1
            # break
            element_nextpage = browser.find_element_by_id("nextLink")
            # element_nextpage.click()
            nextLink = str(element_nextpage.get_attribute("href"))
            # print nextLink
            with open("info.txt", "w") as fb:
                fb.write(nextLink)
            # element_content.send_keys(Keys.LEFT)
            browser.quit()
            time.sleep(1)
            print "exit success!"
            time.sleep(2)
            break
            # time.sleep(random.randint(1, 4))
            # break
            # time.sleep(1)
        except Exception as e:
            browser.quit()
            print e
            break

    
if __name__ == '__main__':
    getNovel()
