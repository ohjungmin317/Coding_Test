# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:44:09 2022

@author: 오정민
"""

n = int(input())

array=[]

for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda student: student[1])
# lambda는 이름이 없는 함수를 만들 수 있음 
# 인자로 받은 동시에 바로 사용이 가능하다.

for student in array:
    print(student[0], end=' ')

# n = int(input())

# array = []

# for i in range(n):
#     data = input().split()
#     array.append((data[0], int(data[1])))
    
# def x(array) :
#     return array[1]

# array = sorted(array, key=x)

# for i in array:
#     print(i[0], end=' ')