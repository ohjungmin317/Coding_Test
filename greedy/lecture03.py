# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 17:13:55 2022

@author: 오정민
"""
# p311 모험가 길드

# (1) 입력된 값을 오름차순으로 정렬을 해준다. 
# (2) 해당 공포도를 하나씩 확인하며 '현재 그룹에 포함이 된 모험가의 수' 가 현재 확인하고 있는 공포도 보다
# 크거나 같다면 이를 그룹으로 설정을 해주면 된다. 

data = int(input())

result = list(map(int, input().split()))

result.sort()

group_mem = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수  / 그룹이 결성이 되면 0이 되게 한다.

#print(result)

for i in result : # 공포도를 하나씩 확인 (입력된 값을 하나씩 확인하면서)
    count = count + 1 # 현재 그룹에 포함된 모험가 포함
    if count >= i: # 그룹에 포함이된 모험가가 현재의 공포도 이상이라면 모험가 결성
        group_mem = group_mem +1 # 모험가의 수 count 하나씩 증가를 시킨다.
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화 
    
print(group_mem)