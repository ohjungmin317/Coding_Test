# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 16:19:46 2022

@author: 오정민
"""
# # 재귀함수를 이용하여 피보나치 수열 -> 수가 커지면 시간복잡도에 있어 비효율적이다
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x -1) + fibo(x - 2)

# print(fibo(4))


# DP를 이용하여 피보나치 수열 TOP-DOWN
# d = [0] * 100 # -> 한 번 계산된 결과를 메모이제이션 하기 위해 리스트 초기화

# def fibo(x):
#     if x == 1 or x == 2: # 종료조건
#         return 1 
#     if d[x] !=0: # 이미 계산한 적이 있는 문제이면 그대로 반환 
#         return d[x]
    
#     d[x] = fibo(x-1) + fibo(x-2) # 아직 계산하지 않은 문제이면 점화식에 따라 피보나치 결과 반환
#     return d[x]

# print(fibo(99))

# # DP를 이욯아여 피보나치 수열 BOTTOM-UP
# d = [0] * 100

# # 첫번째와 두번째는 1로 초기화 
# d[1] = 1
# d[2] = 1
# n = 99

# # 피보나치 함수 반복문으로 구현(bottom-up dynaimc programming)
# for i in range(3, n+1): # 1과 2는 1 이기 때문에 i값이 3부터 시작해서 n+1 하나씩 증가
#     d[i] = d[i-1] + d[i-2]

# print(d[n])


# 메모이제이션 동작 - 피보나치 수열

d = [0] * 100

def fibo(x):
    print('f(' + str(x) +')', end =' ')
    if x == 1 or x == 2:
        return 1
    if d[x] !=0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(6)

# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4) 










