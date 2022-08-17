# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:10:23 2022

@author: 오정민
"""

# 특정 원소가 속한 집합 찾기 : 개선된 서로소 집합 알고리즘 
def find_road(road, x):
    if road[x] != x:
        road[x] = find_road(road, road[x])
    return road[x]

def union_road(road,a,b):
    a = find_road(road, a)
    b = find_road(road, b)
    
    if a < b:
        road[b] = a
    else:
        road[a] = b

n,m = map(int, input().split())

road = [0] * (n+1) # 부모 테이블 초기화 (0으로)

# 모든 간선을 받을 리스트(배열) 과 최종 비용을 담을 변수 
edges=[]
result = 0

# 부모 자기 자신으로 초기화 
for i in range(1, n+1):
    road[i] = i

for _ in range(m):
    a,b,c = map(int, input().split())
    
    # 비용순으로(c) 정렬하기 위하여 튜플의 첫 번째 원소를 비용으로 설정 
    edges.append((c, a, b))

# 최소 신장 트리에서는 해당 비용을 sort(정렬)을 해줘야 한다.    
edges.sort()
# 가장 큰 간선의 길이를 구해야 한다. 
big_num = 0

for edge in edges:
    c, a, b = edge
    
    # 크르수칼 ( 최소 신장 트리 ) 조건이 사이클이 발생하지 않을 조건이기 때문에 사이클이 발생하지 않을때 집합에 포함 
    if find_road(road, a) != find_road(road, b):
        union_road(road, a, b)
        result = result + c
        # 가장 큰 간선의 값을 big_num에 넣어놓기 
        big_num = c
# 최종 결과는 총 간선의 길이에서 가장 큰 간선의 길이를 뺀 것이 답이 된다. 
print(result - big_num)

        