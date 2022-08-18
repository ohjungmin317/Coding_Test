# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 19:28:33 2022

@author: 오정민
"""

import heapq

n,m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1

def topology_sort():
    result=[]
    heap =[]
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(heap,i)
            
    while heap:
        
        now= heapq.heappop(heap)
        result.append(now)
        
        for i in graph[now]:
            indegree[i] = indegree[i] -1
            
            if indegree[i] == 0:
                heapq.heappush(heap, i)
    
    for i in result:
        print(i, end=' ')

topology_sort()
        