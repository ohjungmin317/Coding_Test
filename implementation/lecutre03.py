# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:21:44 2022

@author: 오정민
"""

area = list(input())

x = int(area[1])
y = ord(area[0]) -96

step = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)] # 두개의 리스트가 아닌 한가지 리스트로도 이용할 수 있다.

# 두개의 리스트로 해결을 하는 방법 
# dx = [-1,1,2,2,1,-1,-2,-2]
# dy = [2,2,1,-1,-2,-2,-1,1]


result = 0

for i in step:
    # 이동하고자 하는 위치 확인 
    next_step1 = x + i[0]
    next_step2 = y + i[1]
    
    # 해당위치로 이동하였을 때 (이동할 수 있는 위치) -> 카운트 증가 
    if next_step1 >=1 and next_step1 <=8 and next_step2 >=1 and next_step2 <=8:
        result = result+1

print(result)
