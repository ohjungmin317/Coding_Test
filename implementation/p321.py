# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:19:51 2022

@author: 오정민
"""

# p321 - 럭키스트레이트 

n = input()

sum_1 = 0
sum_2 = 0

for i in range(len(n) // 2):
    sum_1 = sum_1 + int(n[i])

for i in range(len(n) // 2, len(n)):
    sum_2 = sum_2 + int(n[i])
    

if sum_1 == sum_2:
    print("LUCKY")
else:
    print("READY")
