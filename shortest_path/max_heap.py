# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 16:12:09 2022

@author: 오정민
"""

import heapq

# 내림차순 힙 정렬

n = list(map(int, input().split()))

def heapsort(iterable):
    h=[]
    result=[]
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
        
    # 힙에 삽입된 모든 원소들을 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    
    return result

result = heapsort(n)
print(result)