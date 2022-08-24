# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:48:47 2022

@author: 오정민
"""

# 11660 - 구간 합 구하기 - dp 문제 해결 

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

s1 =[]
dp =[[0] * (n+1) for i in range(n+1)]

for _ in range(n):
    s1.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + s1[i-1][j-1]

for a in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    
    result = dp[x2][y2] - dp[x2][y1 -1] - dp[x1 -1][y2] + dp[x1-1][y1-1]
    print(result)
        
    
