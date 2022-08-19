# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 17:18:41 2022

@author: 오정민
"""

# p393

def find_parent(parent,x):
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

n,m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i


for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == True:
            union_parent(parent, i+1, j+1)

plan = list(map(int,input().split()))

result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("Yes")
else:
    print("No")