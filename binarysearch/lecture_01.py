# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:49:36 2022

@author: 오정민
"""

# p201 떡볶이 떡 만들기

n,m = map(int,input().split())

array = list(map(int,input().split()))


start = 0

end = max(array)

result = 0

while (start <= end):
    target = 0
    mid = (start+end) // 2
    
    for a in array:
        if a>mid:
            target += a-mid
    
    if target < m:
        end = mid -1
    
    else:
        result = mid
        end = mid + 1
print(result)
            
    
    