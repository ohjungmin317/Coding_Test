# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:39:36 2022

@author: 오정민
"""
# p380 병사 배치하기 
# 문제 아이디어 : 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열로 알려진 전형적인 다이나믹
# 프로그래밍 문제의 아이디어와 같다. (LIS 알고리즘과 같다.)

# 점화식:
    # D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
    # -> 모든 0<=j<i 에 대해서 D[i] = max(D[i], D[j] + 1) if array[j] < array[i] 
    # (cf. 앞에 있는 원소가 뒤에 있는 원소보다 작을 때 위 점화식을 사용할 수 있다.)
    

n = int(input())

array = list(map(int, input().split()))

array.reverse()

d = [1] * n


for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            d[i] = max(d[i],d[j]+1)

print(n-max(d)) # 원래 n에서 -  가장 긴 값이 해당 배열의 길이 값 


# LIS 문제
n = int(input())

array = list(map(int, input().split()))

d = [1] * n

for i in range(1,n):
    for j in range(0, i):
        if array[j] < array[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

print(max(d))