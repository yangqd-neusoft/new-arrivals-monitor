# new-arrivals-monitor
Monitor the new arrivals of “xiao mian ao”, send a mail to Qian when there are some new arrivals, which includes graphics and text information.

## crawler`关键点`：
* 1.商品编号
* 2.遍历页面内的商品
* 3.图文信息

[百度](https://www.baidu.com "baidu")
![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")
[百度](https://www.baidu.com "baidu")

## 关于动态js页面的爬取，方案一：
* 1.lxml与BeautifulSoup的选择，lxml利用元素遍历法来处理数据，BeautifulSoup利用正则表达式来提取数据
* 2.Web kit属于QT库的一部分，安装QT和PyQT4库，可以实现浏览器所能处理的任何事情
* 3.通过Web kit发送请求信息，等待网页被完全加载后将其赋值到某个变量中，再利用lxml从HTML数据中提取有效信息
  ```python
  import sys
  from PyQt4.QtGui import *
  from PyQt4.Qtcore import *
  from PyQt4.QtWebKit import *
  class Render(QWebPage):
    def __init__(self, url):
      self.app = QApplication(sys.argv)
      QWebPage.__init__(self)
      self.loadFinished.connect(self._loadFinished)
      self.mainFrame().load(QUrl(url))
      self.app.exec_()
    def _loadFinished(self, result):
      self.frame = self.mainFrame()
      self.app.quit()
  url = 'http://pycoders.com/archive/'
  # This does the magic.Loads everything
  r = Render(url)
  # Result is a QString.
  result = r.frame.toHtml()
  
* 4.以上的代码，将HTML结果储存到变量result中，lxml无法直接处理该特殊的字符串数据，需要转换数据格式
  ```python
  # QString should be converted to string before processed by lxml
  formatted_result = str(result.toAscii())
  # Next build lxml tree from formatted_result
  tree = html.fromstring(formatted_result)
  # Now using correct Xpath we are fetching URL of archives
  archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
  print archive_links
  ```

## 关于动态js页面的爬取，方案二：
* 1.python可以使用selenium执行javascript，selenium可以让浏览器自动加载页面，获取需要的数据，selenium自己不带浏览器，可以使用第三方浏览器如Firefox，Chrome等，也可以使用headless浏览器如PhantomJS在后台执行
  ```python
  #/usr/bin/python
  from urllib import request
  from lxml import etree
  from selenium import webdriver
  import time

  # 京东手机商品页面
  url="http://item.jd.com/1312640.html"

  # 下面的xslt是通过集搜客的谋数台图形界面自动生成的
  xslt_root = etree.XML("""\
  <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >
  <xsl:template match="/">
  <商品>
  <xsl:apply-templates select="//*[@id='itemInfo' and count(.//*[@id='summary-price']/div[position()=2]/strong/text())>0 and count(.//*[@id='name']/h1/text())>0]" mode="商品"/>
  </商品>
  </xsl:template>

  <xsl:template match="//*[@id='itemInfo' and count(.//*[@id='summary-price']/div[position()=2]/strong/text())>0 and count(.//*[@id='name']/h1/text())>0]" mode="商品">
  <item>
  <价格>
  <xsl:value-of select="*//*[@id='summary-price']/div[position()=2]/strong/text()"/>
  <xsl:value-of select="*[@id='summary-price']/div[position()=2]/strong/text()"/>
  <xsl:if test="@id='summary-price'">
  <xsl:value-of select="div[position()=2]/strong/text()"/>
  </xsl:if>
  </价格>
  <名称>
  <xsl:value-of select="*//*[@id='name']/h1/text()"/>
  <xsl:value-of select="*[@id='name']/h1/text()"/>
  <xsl:if test="@id='name'">
  <xsl:value-of select="h1/text()"/>
  </xsl:if>
  </名称>
  </item>
  </xsl:template>
  </xsl:stylesheet>""")

  # 使用webdriver.PhantomJS
  browser=webdriver.PhantomJS(executable_path='C:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
  browser.get(url)
  time.sleep(3)

  transform = etree.XSLT(xslt_root)

  # 执行js得到整个dom
  html = browser.execute_script("return document.documentElement.outerHTML")
  doc = etree.HTML(html)
  # 用xslt从dom中提取需要的字段
  result_tree = transform(doc)
  print(result_tree)
  ```

## PS：
* 1.操作工具  Pyv8，PythonWebKit，Selenium，PhantomJS，Ghost.py  等等。。。。
* 2.[静觅博客](http://cuiqingcai.com/ "博客")
