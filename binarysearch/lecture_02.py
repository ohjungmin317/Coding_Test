# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:32:17 2022

@author: 오정민
"""

# p197 부품찾기

# Binary search 방법으로 해결 

n = int(input()) # 가게에 가지고 있는 부품의 개수 

question_array = list(map(int,input().split())) # 각 부품에 대한 종류 

question_array.sort() # binary search를 해주기 위해서는 가장 기본적인 조건인 sort를 해줘야 하기 때문에 sort 함수를 사용 

m = int(input()) # 소비자가 원하는 부품의 개수 

collect_array = list(map(int,input().split())) # 소비자가 원하는 부품의 종류 


def binary_search(array,target,start,end): # 이진탐색 정의 ( 반복문 조건 )
    while(start<=end): 
        mid = (start+end)//2 # 중간값 구하기 
        
        if array[mid] == target: # 찾고자 하는 값이 중간값과 같을 때에는 중간값 출력 
            return mid
        elif array[mid] > target: # 중간값보다 원하는 값이 더 작으면 
            end = mid - 1 # 왼쪽으로 탐색 
        else: # 중간값보다 원하는 값이 더 크면 
            start = mid + 1 # 오른쪽 탐색 
    
    return None

for i in collect_array: # 소비자가 원하는 부품 하나씩 탐색 하는 반복문 
    
    result = binary_search(question_array, i, 0, n-1)
    
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# Set 방법으로 풀어보기

# n = int(input())

# question_array = set(map(int,input().split()))

# m = int(input())   

# collect_array = list(map(int, input().split()))


# for i in collect_array:
#     if i in question_array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

