# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:52:34 2022

@author: 오정민
"""
# start -> 오른쪽 / end - 왼쪽
def binary_search(array, target, start, end):
    if start > end:
        return None
    
    # 찾은 경우 중간점 인덱스 반환  //-> 중간점 식
    mid = (start + end) // 2 
    
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

n, target = map(int,input().split())

# 배열을 입력할깨에는 무조건 정렬된 것만 출력  
array = list(map(int,input().split()))

# 이진탐색 결과 출력
result = binary_search(array, target, 0, n-1)

print(result + 1)


# 반복문으로 이진탐색 하기 
# def binary_search(array, target, start, end):
#     while start<= end:
#         mid = (start+end) // 2
        
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

# n, target = map(int,input().split())

# # 배열을 입력할깨에는 무조건 정렬된 것만 출력  
# array = list(map(int,input().split()))

# # 이진탐색 결과 출력
# result = binary_search(array, target, 0, n-1)

# print(result + 1)
   
