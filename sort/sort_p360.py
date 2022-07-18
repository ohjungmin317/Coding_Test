# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:23:14 2022

@author: 오정민
"""

# p360 안테나
# 최소가 되려면 해당 값에 대해 정렬을 해준다음 중간값을 구해주어서 출력을 해주면 된다. 

# n = int(input())

# array = list(map(int, input().split()))
    
# array.sort()

# print(array[(n-1)//2])
# 중간값 구하는 법 // 기호 사용



# 중앙값 사용하는 법 
# import statistics

# statistics.median(data 값) 

n = int(input())

array=[]

for i in range(n):
    data = input().split()
    array.append((int(data[0]),data[1]))

array = sorted(array, key=lambda student: student[0])

for student in array:
    print(student[0],student[1])
