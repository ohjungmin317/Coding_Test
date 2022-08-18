# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:28:23 2022

@author: 오정민
"""

from collections import deque
import copy


# 개수 입력 받기 (과목 개수 = 노드 개수)
n = int(input())

# 모든 노드에 대해 진입차수 0으로 초기화
indegree = [0] * (n+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 ( 그래프 ) 초기화 
graph = [[] for i in range(n+1)]

# 각 강의 시간 (time) 0으로 초기화 
time = [0] * (n+1)

# 방향 그래프의 모든 간선 정보 입력을 받기 
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음 
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)

# 위상 정렬 함수 
def topology_sort():
    result= copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # queue를 사용하기 위해 deque라이브러리 사용 
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    # q가 빌때까지 반복 
    while q:
        now = q.popleft()
        
        # 해당 원소와 연결된 노드들의 진입차수에서 -1 
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -=1
            
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n+1):
        print(result[i])

topology_sort()