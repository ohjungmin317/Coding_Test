# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:28:59 2022

@author: 오정민
"""

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index # 데이터의 개수를 반환하는 함수 빼주면 된다.

a = [1 , 2 , 3 , 3 , 3 , 3 , 4 , 4 , 8 , 9]

#[4,4]

print(count_by_range(a, 4, 4))

#[-1,3]
print(count_by_range(a, -1, 3))

