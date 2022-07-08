# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:49:37 2022

@author: 오정민
"""
# P110 상하좌우

# 좌표 (1,1) 인 경우에는 첫 번째 것은 사용을 하지 않는다.
# 시작 좌표가 (1,1) -> 가장 왼쪽 위가 시작점이다.
# 공간을 벗어나게 되면 무시 된다. 

num = int(input())
result = input().split()
x, y = 1, 1

type = ['L','R','U','D']

for i in range (len(result)):
    if result[i] == type[0]:
        if y - 1 == 0:
            continue
        else:
            y = y - 1
    if result[i] == type[1]:
        if y + 1 == num + 1:
            continue
        else:
            y = y + 1
    if result[i] == type[2]:
        if x - 1 ==0:
            continue
        else:
            x = x - 1
    if result[i] == type[3]:
        if x + 1 == num + 1:
            continue
        else:
            x = x + 1

print(x, y)
        
    
        


# print(array)
