# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:32:13 2022

@author: 오정민
"""

def dfs(graph, v, visited):
    
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문처리
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph =[
        [], # 0번째 노드
        [2, 3, 8], # 1번째 노드가 연결된 노드
        [1, 7], # 2번째 노드가 연결된 노드
        [4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]  # 8번째 노드가 연결된 노드
        ]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)