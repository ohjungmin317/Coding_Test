# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 17:08:50 2022

@author: 오정민
"""

# p466

# 소수 : 1보다 큰 자연수 중에 1과 자기 자신을 제외한 자연수로 나누어 떨어지지 않는 자연수

def is_prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

print(is_prime_num(4))
print(is_prime_num(7))

# 소수 판별 알고리즘 시간복잡도 : 2부터 x-1까지 자연수에 대해 연산을 수행하게 되면 : O(X)이다.

# 시간 줄이기 방법 : 약수의 성질 이용
