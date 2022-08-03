# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:23:25 2022

@author: 오정민
"""
# p217 1로 만들기


n = int(input())

d = [0] * 30001

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    
    # 현재 수에서 5로 나눠 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
    # 현재 수에서 3으로 나눠 떨어지는 경우
    elif i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    # 현재의 수에서 2로 나눠 떨어지는 경우 
    elif i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        
print(d[n])

# 점화식 : a[i] = min(a[i-1], a[i//2], a[i//3], a[i//5])
# +1을 하는 이유 ? -> 개수를 구해야하기 때문에 +1을 해줘야 한다. 


# # 백준 1로 만들기
# n = int(input())

# dp = [0] * (n+1)

# for i in range(2, n+1):
#     dp[i] = dp[i-1] + 1
    
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
        
# print(dp[n])
    