# new-arrivals-monitor
Monitor the new arrivals of “xiao mian ao”, send a mail to Qian when there are some new arrivals, which includes graphics and text information.

## crawler`关键点`：
* 1.商品编号
* 2.新品页面的第一个商品
* 3.当前商品按顺序的下一个商品
* 4.图文信息

[百度](https://www.baidu.com "baidu")
![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")
[百度](https://www.baidu.com "baidu")

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
```
## 关于动态js页面的爬取：
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
  ```
  ```python
  url = 'http://pycoders.com/archive/'
  # This does the magic.Loads everything
  r = Render(url)
  # Result is a QString.
  result = r.frame.toHtml()
  ```
  以上的代码，将HTML结果储存到变量result中，lxml无法直接处理该特殊的字符串数据，需要转换数据格式
  ```python
  # QString should be converted to string before processed by lxml
  formatted_result = str(result.toAscii())
  # Next build lxml tree from formatted_result
  tree = html.fromstring(formatted_result)
  # Now using correct Xpath we are fetching URL of archives
  archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
  print archive_links
  ```
