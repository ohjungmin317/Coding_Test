# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:16:55 2022

@author: 오정민
"""
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화를 해준다.)
count = [0] * (max(array)+1)  

for i in range(len(array)): # 각 데이터에 해당하는 인덱스 값 증가
    count[array[i]] = count[array[i]] + 1
    
for i in range(len(count)): # 리스트에 기록이된 정렬 정보 확인 
    for j in range(count[i]):
        print(i,end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력    
