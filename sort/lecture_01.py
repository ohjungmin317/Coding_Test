# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:37:16 2022

@author: 오정민
"""

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))
    
array = sorted(array, reverse=True)

#print(array)

for i in array:
    print(i, end=' ')


# 선택정렬로 풀어 본 것 
# n = int(input())

# array=[]

# for i in range(n):
#     array.append(int(input()))

# for i in range(len(array)):
#     min_array = i
#     for j in range(i+1, len(array)):
#         if array[min_array] > array[j]:
#             min_array = j
#     array[i], array[min_array] = array[min_array], array[i] # swap
    
# for i in array:
#     print(i, end=' ')