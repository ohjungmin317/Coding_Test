# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:11:08 2022

@author: 오정민
"""
# p113 시각
#Brute force algorithm을 이용하여 해결
# 하나씩 모두 세서 풀 수 있는 문제
# -> 24 * 60 * 60 = 86400
# 단순하게 시각을 1씩 증가시켜서 3이 하나라도 포함이 되는지 확인하면 된다.

num = int(input())
result = 0

for i in range(num+1):
    for j in range(60):
        for k in range(60):
                if '3' in str(i) + str(j) + str(k): # 매 시각 안에 '3이 포함이 되어 있으면 카운트 증가 
                    result = result + 1
print(result)
    