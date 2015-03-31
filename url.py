#!/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handler.admincontent import AdminHandler

url = [
    (r"/admincontent", AdminHandler),
]
