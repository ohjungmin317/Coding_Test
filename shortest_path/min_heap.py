# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:05:53 2022

@author: 오정민
"""

import heapq # 힙 라이브러리 

# 오름차순 힙 정렬(heap sort)

n = list(map(int, input().split()))

def heapsort(iterable): # list / tuple 같은 iterable과 같은 값이 들어오게 되면 
    h=[]
    result=[]
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort(n)
print(result)