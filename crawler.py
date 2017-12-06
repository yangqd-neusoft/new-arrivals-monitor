#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from database import SQLite
from mail import sendMail

URL = ""
PATH_DB = ""
PATH_LOG = ""
LIST_DIR = []
TIME_SPACE = 600

SQLite_inst = SQLite(PATH_DB)
SQLite_inst.connectToDB()

def saveDataID():
    saveDB_count = 1
    browser = webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    try:
        browser.get(URL)
    except Exception as e:
        browser.quit()
        fo = open(PATH_LOG, "a")
        fo.write( time.asctime(time.localtime(time.time())) + ' ' + str(e) + '\n' )
        fo.close()
        return
    time.sleep(3)
    while True:
        elements_item3line1s = browser.find_elements_by_class_name("item3line1")
        for item3line1 in elements_item3line1s:
            elements_items = item3line1.find_elements_by_tag_name("dl")
            for dl in elements_items:
                dataID = dl.get_attribute("data-id")
                if not SQLite_inst.select(dataID):
                    SQLite_inst.insert(dataID)
        saveDB_count = saveDB_count+1
        try:
            element_pagelink = browser.find_element_by_link_text("%s" % str(saveDB_count))
            element_pagelink.click()
            time.sleep(3)
        except Exception as e:
            fo = open(PATH_LOG, "a")
            fo.write( time.asctime(time.localtime(time.time())) + ' ' + str(e) + '\n' + "Completed save of %s pages of commodity dataID" % str(saveDB_count) + '\n' )
            fo.close()
            break
    browser.quit()

def monitorNew():
    while True:
        browser = webdriver.PhantomJS(executable_path='D:\\Python27\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
        try:
            browser.get(URL)
        except Exception as e:
            browser.quit()
            fo = open(PATH_LOG, "a")
            fo.write( time.asctime(time.localtime(time.time())) + ' ' + str(e) + '\n' )
            fo.close()
            return
        time.sleep(3)
        first_item3line1 = browser.find_element_by_class_name("item3line1")
        first_item = first_item3line1.find_element_by_tag_name("dl")
        dataID = first_item.get_attribute("data-id")
        if not SQLite_inst.select(dataID):
            fo = open(PATH_LOG, "a")
            fo.write( time.asctime(time.localtime(time.time())) + " There are some new arrvals!" + '\n' )
            fo.close()
            dirList = []
            flag_break = False
            elements_item3line1s = browser.find_elements_by_class_name("item3line1")
            for item3line1 in elements_item3line1s:
                if flag_break: break
                elements_items = item3line1.find_elements_by_tag_name("dl")
                for dl in elements_items:
                    if flag_break: break
                    dataID = dl.get_attribute("data-id")
                    if not SQLite_inst.select(dataID):
                        os.mkdir(dataID)
                        dirList.append(dataID)
                        img = dl.find_element_by_tag_name("img")
                        text = img.get_attribute("adl")
                        fo = open("info.txt", "wb")
                        fo.write(text)
                        fo.close()
                        imgURL = "https:"+img.get_attribute("src")
                        imgRequest = requests.get(imgURL)
                        image = imgRequest.content
                        fo = open("photo.jpg", "wb")
                        fo.write(image)
                        fo.close()
                        SQLite_inst.insert(dataID)
                    else:
                        flag_break = True
            if dirList != []:
                sendMail_inst = sendMail(dirList=dirList)
                sendMail_inst.buildMSG()
                sendMail_inst.sendMail()
        browser.quit()
        time.sleep(TIME_SPACE)


if __name__ == '__main__':
    saveDataID()
    # monitorNew()
    pass
