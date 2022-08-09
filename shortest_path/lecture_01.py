# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 17:24:38 2022

@author: 오정민
"""

# p262 - 전보 
# 핵심 아이디어 : 
    # 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있다.
    # N과 M의 범위가 충분히 크기 때문에 우선순위 큐로 활용한 다익스트라 알고리즘을 구현한다.

import heapq # 힙을 이용한 우선순위 다엑스트라 알고리즘 
import sys
input = sys.stdin.readline
INF = int(1e9)


# 노드의 개수 간선의 개수 시작 노드를 입력받기 
N, M, C = map(int, sys.stdin.readline().rstrip().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기 
graph = [[]for _ in range(N+1)]

# 최단 거리 테이블을 모두 무한대로 초기화 
distance = [int(1e9)] * (N+1)

# 모든 간선 정보를 입력받기
for _ in range(M):
    # start 노드에서 end 노드로 가는 비용이 cost라는 의미 
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((end,cost))
    

def dijkstra(start):
    distance[start] = 0
    q=[]
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 Queue에 삽입
    
    heapq.heappush(q, (0, start))
    
    while q: # q가 비어있지 않다면  
        
        cost , now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기 
        
        if(cost > distance[now]):
            continue
        
        for neighbor in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인 
            
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 
            if(distance[neighbor[0]] > cost + neighbor[1]):
                
                distance[neighbor[0]] = cost + neighbor[1]
                
                heapq.heappush(q, (cost + neighbor[1], neighbor[0]))

# 다엑스트라 알고리즘 수행 
dijkstra(C)

# 도달 할 수 있는 노드의 개수 
count = 0

# 도달 할 수 있는 노드 중에서 가장 멀리 있는 노드와의 최단 거리 
max = 0

# 도달 할 수 있는 노드인 경우 
for d in distance:
    if(d < int(1e9)):
        count = count + 1
        # 가장 거리가 먼 거리를 기록해야 한다. 
        if(d > max):
            max = d
# 시작 노드는 제외해야 함으로 count -1 을 출력 
print(count - 1, max)
    