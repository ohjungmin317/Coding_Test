# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 17:03:10 2022

@author: 오정민
"""

# 두 배열의 원소 교체 
# 문제 해설 : 배열 A에서 가장 작은 원소를 골라 배열 B에서 가장 큰 원소를 교체를 한다.
# -> a에 대한 오름차순 정렬 b에 대해서 내림차순 정렬
# -> k번 횟수를 이용하여 a배열에 있는 것에 비해 b배열에 있는 것이 더 작을 때 swap을 해주면 된다.


n,k = map(int,input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)


for i in range(k):
    if a[i] < b[i]:
        a[i] =  b[i] # swap 함수 
    
    else:
        break

print(sum(a))

        