# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 16:10:08 2022

@author: 오정민
"""
# 1. 행성 좌표를 입력받습니다.

# 2. x, y, z 좌표별로 각각 정렬한 후 각 행성 사이의 거리를 구합니다.

# 3. 가장 작은 거리부터 사이클을 확인한 후 연결하는 크루스칼 알고리즘을 사용하여 최소 스패닝 트리를 구합니다.



import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

parent = [0] * (n+1)

edges=[]
temp=[]
result = 0

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    a,b,c = map(int, input().split())
    temp.append((a,b,c,i))
    
for i in range(3):
    temp.sort(key=lambda x:x[i])
    for j in range(1, n):
        edges.append((abs(temp[j-1][i]-temp[j][i]),temp[j-1][3],temp[j][3]))

edges.sort()

for i in range(len(edges)):
    if find_parent(parent, edges[i][1]) != find_parent(parent, edges[i][2]):
        union_parent(parent, edges[i][1], edges[i][2])
        result += edges[i][0]

print(result)