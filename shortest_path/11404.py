# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 19:29:48 2022

@author: 오정민
"""
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    if graph[a][b] > c: # 기존 플로이드 와샬 알고리즘과 다른 것 최소인 경우에 저장을 해야하기 때문에 위 조건문을 걸어줘야 한다.
        graph[a][b] = c
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end= " ")
    
    print()