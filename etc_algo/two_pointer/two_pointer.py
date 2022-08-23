# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 16:27:43 2022

@author: 오정민
"""

# 투 포인터 알고리즘은 리스트에 순차적으로 접근해야 할 때 두 개의 점의 위치를 기록하면서 처리하는 알고리즘
# 흔히 2 3 4 5 6 7 => 2 ~ 7 까지 학생
# 리스트에 담긴 데이터에 순차적으로 접근해야 할 때 시작점과 끝점 2개의 점으로 접근할 데이터의 범위를 표현 가능 

# 대표적인 문제 ! : 특정한 합을 가지는 부분 연속 수열 찾기 
# -> 1) N개의 자연수로 구성된 수열이 있다.
#    2) 합이 M인 부분 연속 수열의 개수를 구해봐라
#    3) 수행시간 제한 시간복잡도 O(n) 이다. 

# 알고리즘 방법
# 1) 시작점과 끝점이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
# 2) 현재 부분 합이 M과 같다면 카운트 한다.
# 3) 현재 부분 합이 M보다 작다면 end를 1 증가시킨다.
# 4) 현재 부분 합이 M보다 크거나 같다면 start 1 증가시킨다.
# 5) 모든 경우를 확인할 때까지 2번부터 4번까지 과정을 반복한다. 

n,m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end +=1
    
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)