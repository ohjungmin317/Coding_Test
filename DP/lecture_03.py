# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:10:41 2022

@author: 오정민
"""

# p226 효율적인 화폐 구성 

n,m = map(int,input().split())

# N개의 화폐 단위 정보를 입력받기
arr=[]

for i in range(n):
    arr.append(int(input()))

d = [10001] * (m+1) # 초기화 -> 10001로 나타낸다. (초기리스트값)

d[0] = 0

# i = 화폐의 단위 / j = 금액을 의미 
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j - arr[i]] != 10001: # (i-k) 원을 만드는 방법이 존재하는 경우 -> 10001이 아닌경우
            d[j] = min(d[j], d[j-arr[i]]+1) # 점화식 사용 

if d[m] == 10001:
    print(-1)

else:
    print(d[m])
    