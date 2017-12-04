# python 3.5.2
from selenium import webdriver  
import time  
import urllib


# 爬取页面地址  
url = "https://stocksnap.io/"

# 目标元素的xpath  
xpath = "/html/body/div[4]/div[3]/div[2]/div//a/img"

# 启动Firefox浏览器  
driver = webdriver.Firefox()  

# 最大化窗口，因为每一次爬取只能看到视窗内的图片  
driver.maximize_window()  

# 记录下载过的图片地址，避免重复下载  
img_url_dic = {}  

# 浏览器打开爬取页面  
driver.get(url)  

# 模拟滚动窗口以浏览下载更多图片  
pos = 0  
m = 0 # 图片编号  
for i in range(10):  
    pos += i*500 # 每次下滚500  
    js = "document.documentElement.scrollTop=%d" % pos  
    driver.execute_script(js)  
    time.sleep(1)     

    for element in driver.find_elements_by_xpath(xpath):  
        img_url = element.get_attribute('src')  
        # 保存图片到指定路径  
        if img_url != None and not img_url in img_url_dic:

            img_url_dic[img_url] = ''  
            m += 1  
            ext = img_url.split('.')[-1]  
            filename = str(m) + '.' + ext  
            #保存图片数据  
            data = urllib.request.urlopen(img_url).read()
            f = open('./van/' + filename, 'wb')
            f.write(data)  
            f.close()  
driver.close()
