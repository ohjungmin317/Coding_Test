# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:36:42 2022

@author: 오정민
"""

# 만들수 없는 금액

##### 문제 #####

# N개의 동전이 주어질 때, 이 동전들로 만들 수 없는 양의 정수 금액 중 
# 최솟값을 구하는 프로그램을 작성하시오.

n = int(input())

arr = list(map(int, input().split()))

arr.sort() # target은 금액 1부터 시작하고 화폐 단위는 오름차순으로 정렬을 해준다. 

target = 1 # target은 1부터 시작 

for i in range(n):
    if target < arr[i]: # target이 배열에 있는 값보다 큰 경우에는 break를 해준다.
        break
    
    target = target + arr[i] # target을 만들 수 있는 경우에는 화폐 단위를 더해준다.

print(target) # target을 출력 
