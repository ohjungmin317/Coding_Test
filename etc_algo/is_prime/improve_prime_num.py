# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:13:33 2022

@author: 오정민
"""

# p467

import math

def improve_is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
print(improve_is_prime_num(4))
print(improve_is_prime_num(7))

# 개선된 소수 판별 알고리즘 시간 복잡도 : 
    # 2부터 x의 제곱근까지의 모든 자연수에 대해 연산을 수행해야 하면
    # -> 시간복잡도 : O(N^1/2) 입니다.