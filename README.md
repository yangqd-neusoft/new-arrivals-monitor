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
import sys
import json
```
