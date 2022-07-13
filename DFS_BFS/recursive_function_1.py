# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:03:49 2022

@author: 오정민
"""

# 최대 공약수 [유클리드 호제법 계산]
def CDG(a,b) :
    if a % b == 0 :
        return b
    else :
        return CDG(b, a%b)

print(CDG(192, 162))


# 펙토리얼 계산
def fact(n) :
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
        
    
        