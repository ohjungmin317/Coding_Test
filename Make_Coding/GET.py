# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 16:42:33 2022

@author: 오정민
"""

import requests

target = "http://google.com"
response = requests.get(url=target)
print(response.text)