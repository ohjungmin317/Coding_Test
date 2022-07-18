# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:09:32 2022

@author: 오정민
"""

array =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1): # i 부터 출발하여 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] # 자기 보다 크면 SWAP
        else: # 자기 보다 작은 데이터를 만나면 그 위치에서 멈춘다.
            break
print(array)  