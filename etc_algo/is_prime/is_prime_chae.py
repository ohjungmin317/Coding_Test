# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:27:08 2022

@author: 오정민
"""
# p 469 (에라토스테네스의 체 - 다수의 소수 판별)

# 하나의 수에 대해서 소수인지 아닌지 판별하는 방법
# 특정한 수의 범위 안에 존재하는 모든 소수를 찾아야 할때 사용 

# 알고리즘 방법: (N보다 작거나 같은 모든 소수를 찾을 때 사용)
    # (1) 2부터 N까지의 모든 자연수를 나열한다
    # (2) 남은 수 중에서 아직 처리하지 않은 가장 작은수 i를 찾는다.
    # (3) 남은 수 중에서 i의 배수를 모두 제거 한다. (단! i는 제거하지 않는다.) - 제곱근 삭제
    # (4) 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다. 

import math

n = 1000

array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i *j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')