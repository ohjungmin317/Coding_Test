# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:54:53 2022

@author: 오정민
"""
# 구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 때 특저 구간의 모든 수를 합한 값을 계산하는 문제

# 문제 설명
# N개의 정수로 구성된 수열이 있다,
# M개의 query 정보가 주어진다.
    # 각 쿼리는 LEFT / RIGHT으로 나누어진다.
    # 각 쿼리에 대해 [LEFT / RIGHT] 구간에 포함된 데이터들의 합을 출력한다.
# 수행시간은 O(N+M)

# 접두사 합 : 배열의 맨 앞 부터 특정 위치까지의 합을 미리 구해 놓은 것
    # N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장
    # 매 M개의 쿼리 정보를 확인할 때 구간 합은 P[RIGHT] - P[LEFT -1] 이다.

n = int(input())

data = list(map(int, input().split()))

# 접두사 합 배열 계산
sum_value = 0
prefix_sum =[0]

for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
# 구간 합 계산하기 
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left -1])