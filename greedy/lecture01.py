# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:19:43 2022

@author: 오정민
"""

# 1이 될 때 까지 p 99

n, k = map(int, input().split()) # n, k를 공백을 기준으로 구분하여 입력 받기

result = 0


# 시간 복잡도를 log 시간 복잡도로 줄일 수 있다. 
while True:
    
    target = (n // k) * k # target은 k로 나누어 떨어지는 수 
    result += (n - target)
    n = target
    
    if n < k:
        break
    result += 1
    n //= k # n이 k의 배수 일때에는 나눠주면 된다. 
    

result += (n-1)

print(result)


