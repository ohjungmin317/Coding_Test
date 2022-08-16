# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:04:16 2022

@author: 오정민
"""

import json

# 사전 자료형(dictonary) 데이터 선언

user = {
        "id" : "ohjungmin",
        "password" : "12345",
        "age" : 25,
        "hobby" : ["swimming", "programming"]
        }

# 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user, indent=4)  #indent = 들여쓰기 
print(json_data)