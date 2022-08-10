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

# 노드의 개수 및 간선의 개수 입력 받기
n,m = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 ex) (1,1) / (2,2) / (3,3)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 각 간선에 대한 정보를 입력 받아 그 값으로 초기화
for _ in range(m):
    # a와 b는 서로에게 가는 비용은 1이라고 설정
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력 받기     
x,k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행     
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
# 수행된 결과 출력            
distance = graph[1][k] + graph[k][x]

# 도달 할 수 없을 때 무한대 보다 크거나 같을 때에는 -1을 출력 
if distance >= INF:
    print(-1)
# 아니면 결과값을 출력 
else:
    print(distance)
            
            