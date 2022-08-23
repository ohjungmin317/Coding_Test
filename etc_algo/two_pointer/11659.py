# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:31:43 2022

@author: 오정민
"""
import sys
input = sys.stdin.readline

n,m = map(int, input().split())

data = list(map(int, input().split()))

s =[]

sum_value = 0
prefix_sum = [0]


for a in data:
    sum_value += a
    prefix_sum.append(sum_value)


for i in range(m):
    left,right = map(int, input().split())
    print(prefix_sum[right] - prefix_sum[left -1])


        