# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 19:12:24 2022

@author: 오정민
"""
# p259 - 미래도시
# 핵심 아이디어 : 
    # 전형적인 최단 거리 문제이므로 최단 거리 알고리즘을 이용해 해결한다.
    # N의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 이용하여 효율적으로 해결할 수 있다.
    # 플로이드 워셜 알고리즘을 수행한 뒤에 (1번 노드에서 X까지 최단 거리 + X에서 K까지 최단 거리)를 
    # 계산하여 출력하면 정답 판정 

INF = int(1e9)

n,m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x,k = map(int, input().split())
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
            
            