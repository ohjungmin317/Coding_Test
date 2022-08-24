# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:33:32 2022

@author: 오정민
"""

n = int(input())

s = []

def sum_of_sum (x):
    result = 0
    for i in x:
        if i >= '0' and i <= '9':
            result += int(i)
    return result
        

for i in range(n):
    s.append(input().strip())

s = sorted(s, key=lambda x : (len(x), sum_of_sum(x), x))

for i in s:
    print(i)
