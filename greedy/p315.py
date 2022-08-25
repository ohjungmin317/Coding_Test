# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:27:17 2022

@author: 오정민
"""

# 볼링공 고르기 

# n,m = map(int, input().split())

# arr = list(map(int,input().split()))

# count = 0

# for i in range(n):
#     for j in range(i,n):
#         if arr[i] != arr[j]:
#             count = count + 1

# print(count)


n,m = map(int, input().split())
arr = list(map(int, input().split()))
w = [0] * (m+1)

for i in arr:
    w[i] = w[i] + 1

count = 0

for j in range(1, m+1):
    n = n - w[j] # 전체 개수에서 첫번째 사람이 고른 볼링공의 갯수 제외하기
    count = count + w[j] * n # 고르는 개수 count 하기 

print(count)
    