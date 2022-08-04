# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:56:05 2022

@author: 오정민
"""
# p375 금광 

# 문제해결 방법:
    # (1) 왼쪽 위에서 오는 경우
    # (2) 왼쪽 아래에서 오는 경우
    # (3) 왼쪽에서 오는 경우 

# 점화식 -> dp[i][j] = array[i][j] + max(dp[i-1][j-1] + dp[i][j-1] + do[i+1][j-1)]

T = int(input())


for i in range(T):
    n,m = map(int,input().split())
    array = list(map(int, input().split()))
    
    dp=[]
    index = 0
    for i in range(n):
        dp.append(array[index:index + m]) # 2차원 데이터 index로 slice 해주고 + m을 더해서 2차원 배열로 나타낸다.
        index = index + m
    for j in range(1,m):
        for i in range(n):
            
            # 왼쪽 위에 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우 
            left = dp[i][j-1]
            
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)


# DP 테이블을 생성하지 않고 GOLD의 모든 경우의 수를 갱신하여서 푸는 경우의 수 
T = int(input())

for i in range(T):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    
    
    gold = []
    index=0
    for i in range(n):
        gold.append(array[index:index+m])
        index = index + m
    
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위가 값을 벗어나는 경우 
            if i==0:
                gold[i][j] = max(gold[i][j-1]+gold[i][j], gold[i+1][j-1]+gold[i][j])
            
            elif i == n-1:
                gold[i][j] = max(gold[i-1][j-1]+gold[i][j], gold[i][j-1]+gold[i][j])
                
            else:
                gold[i][j] = max(gold[i-1][j-1]+gold[i][j], gold[i+1][j-1]+gold[i][j], gold[i][j-1]+gold[i][j])

    result = 0
    
    for g in gold:
        result = max(result,max(g))
    
    print(result)