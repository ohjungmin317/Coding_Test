# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:57:14 2022

@author: 오정민
"""

array =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_array = i
    for j in range(i+1, len(array)):
        if array[min_array] > array[j]:
            min_array = j
    array[i], array[min_array] = array[min_array], array[i] # swap
    
print(array)

