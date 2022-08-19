# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:43:40 2022

@author: 오정민
"""

# 1922 - 네트워크 연결 ( 크루스칼 알고리즘 )
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
m = int(input())

parent = [0] * (n+1)

edges=[]
result=0

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)