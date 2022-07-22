# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:17:08 2022

@author: 오정민
"""
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index # 데이터의 개수를 반환하는 함수 빼주면 된다.

n,m = map(int,input().split())

array = list(map(int, input().split()))


count = count_by_range(array, m, m)

if (count==0):
    print('-1')

else:
    print(count)


# 이진탐색으로 푼 것 
def binary_search(array, target, start, end): # 이진탐색 정의 된 함수 
    
    while(start<=end):
        mid = (start + end)//2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    
    return 0

n,x = map(int, input().split())

array = list(map(int, input().split()))

start = 0 

end = n - 1

pre_binary = binary_search(array, x-1, start, end) # 이진탐색에서 왼쪽 탐색
post_binary = binary_search(array, x+1, start, end) # 이진탐색에서 오른쪽 탐색 

position = (post_binary-1) - (pre_binary+1) + 1  # postion -> 해당 개수 세기 위한 것 오른쪽에서는 하나 뒤 왼쪽에서는 하나 앞에 그리고 + 1 

if post_binary - pre_binary > 0: # count 개수가 양수인 경우에는 해당 개수 출력 
    print(position)

else: # 아닌 경우에는 -1 출력 
    print(-1)















             