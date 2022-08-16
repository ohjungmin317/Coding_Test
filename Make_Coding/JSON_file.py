# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:07:45 2022

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

# JSON 데이터로 변환하여 파일로 저장
with open("user.json" , "w", encoding="utf-8") as file:
    json_data = json.dump(user, file, indent=4)

# "w" -> 쓰기 권한 / encoding = "utf-8" -> 한글이 포함된 인코딩 방식 