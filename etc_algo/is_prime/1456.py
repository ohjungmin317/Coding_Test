# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:20:39 2022

@author: 오정민
"""
# 거의 소수( 에라토스체 문제 )

import math

a,b = map(int, input().split())

array = [True for a in range(b+1)]

array[1] = False

for i in range(2, int(b ** 0.5)+1):
    if i * i > int(b ** 0.5):
        break
    
    if not array[i]:
        continue
    
    for j in range(i*i, int(b**0.5) +1, i):
        array[j] = False
        
count = 0

for i in range(2, len(array)):
    if array[i]:
        j = i * i
        while True:
            if j < a:
                j *= i
                continue
            if j > b:
                break
            
            j *= i
            count = count + 1

print(count)


# 에라토스테네스의 체 알고리즘 성능
# 선형에 가장 가까울 정도로 시간복잡도가 매우 빠르다 : O(NloglogN) 이다.
# 에라토스테네스의 체 알고리즘은 다수의 소수를 찾아야 하기 때문에 효과적으로 사용이 가능하지만
# 소수 여부를 저장해야하기 때문에 메모리가 많이 필요하다.
