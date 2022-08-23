# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:42:45 2022

@author: 오정민
"""
INF = int(1e9)

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for a in range(n):
    for b in range(n):
        for c in range(n):
            if graph[b][a] and graph[a][c]:
                graph[b][c] = 1

for i in graph:
    for j in i:
        print(j, end=' ')
    print()
