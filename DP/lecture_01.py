# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 17:06:53 2022

@author: 오정민
"""

# p220 개미전사

# 문제 접근 : 
    # (1) 식량창고는 일직선으로 연결이 되어 있다.
    # (2) 서로 인접한 창고는 공격을 할 수 없고 한 칸 이상 떨어진 식량 창고만 공격이 가능하다.
    # (3) 얻을 수 있는 식량의 최댓값을 구해라


n = int(input())
storage = list(map(int, input().split()))

d = [0] * 100 

d[0] = storage[0]
d[1] = max(storage[0], storage[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+storage[i])


print(d[n-1])

# 해당 점화식 : a = max(a(i-1), a(i-2)+ki)
    