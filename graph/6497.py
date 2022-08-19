# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 19:17:02 2022

@author: 오정민
"""

# 6497  - 전력난 ( 크루스칼 알고리즘 )
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

while True:
    n,m = map(int,input().split())
    
    if n == 0 and m == 0:
        break
    
    parent = [0] * (n+1)

    edges=[]
    result=0

    for i in range(1,n+1):
        parent[i] = i
    
    temp=0
    
    for _ in range(m):
        a,b,cost = map(int, input().split())
        edges.append((cost,a,b))
        temp += cost

    edges.sort()

    for edge in edges:
        cost,a,b = edge
        
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(temp-result)