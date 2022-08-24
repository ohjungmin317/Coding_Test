# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:45:48 2022

@author: 오정민
"""
# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때,
#  앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# ex) 5 2
#     4 1 2 3 5

n,a = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

print(arr[a-1])
