# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:38:42 2022

@author: 오정민
"""

# array =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end: # 원소가 1개인 경우에는 return으로 종료 
#         return 
#     pivot = start # 피벗은 첫 번째 원소 
#     left = start + 1 # 가장 왼쪽
#     right = end # 가장 오른쪽
    
#     while(left <= right): # 엇갈리때 까지 반복 -> left의 값보다 right의 값이 더 큰 경우
        
#         while(left<= end and array[left] <= array[pivot]):
#             left = left + 1 # pivot 보다 큰 데이터를 찾을때 까지 반복
        
#         while(right>start and array[right]> array[pivot]):
#             right = right - 1 # pivot 보다 작은 데이터를 찾을때까지 반복  
        
#         if(left>right): # 만약에 left와 right가 엇갈렸다면 작은 데이터와 pivot을 교체
#             array[right], array[pivot] = array[pivot], array[right]
        
#         else: # 엇갈리지 않았따면 작은 데이터와 큰 데이터를 교체
#             array[left], array[right] = array[right], array[left]
    
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬수행 -> 재귀 함수 이용
#     quick_sort(array, start, right -1)
#     quick_sort(array, right+1, end)

# quick_sort(array, 0, len(array)-1)
# print(array)

array =[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    
    # 리스트가 하나인 경우에는 종료 
    if len(array) <=1:
        return array
    pivot = array[0] # pivot은 array 1번째 원소로 지정 
    tail = array[1:] # tail은 pivot을 제외한 리스트 
    
    left_side = [x for x in tail if x<=pivot] # 분할이 된 왼쪽 부분
    right_side = [x for x in tail if x>pivot] # 분할이 된 오른쪽 부분 
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트로 반환 
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
    