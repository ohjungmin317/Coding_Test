# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:49:36 2022

@author: 오정민
"""

# p201 떡볶이 떡 만들기

# 구현방법 : 시작(0) / 끝 (가장 긴 떡의 길이) / 중간 ( 시작 + 끝 ) // 2
# 1) 절단한 떡의 총 길이와 필요한 떡 길이의 비교 
# 2) 절단한 떡이 길이가 부족하면 중간점을 줄인다 ( 왼쪽 탐색 )
# 3) 떡의 양이 충분한 경우 덜 자를 수 있는지 확인해서 최대한 덜 잘라야 한다. ( 오른쪽 탐색 )



n,m = map(int,input().split())# n : 떡의 개수 m : 떡의 길이 

array = list(map(int,input().split())) # 각 떡의 개수에 맞는 개별 높이 입력 


start = 0 # 시작점 (0)

end = max(array) # 끝점 ( 가장 긴 떡의 길이 )

result = 0 # 떡의 최대 길이 

while(start<=end):
    target=0 
    mid = (start+end)//2 # 중간 값 
    for x in array: # 잘랐을 때의 떡의 양 계산
        if x > mid: 
            target += x -mid
            if target > m: # 이미 필요한 만큼의 길이를 넘었다면 더이상 세지 않도록 break해준다.
                break
    
    if target < m: # 떡의 양이 부족한 경우 -> 더 탐색을 할 수 있다면 ( 왼쪽 부분 탐색 )
        end = mid - 1
    
    else: # 떡의 양이 충분해서 더 이상 자르지 않아도 된다고 한다면 ( 오른쪽 부분 탐색 )
        result = mid
        start = mid + 1

print(result) # 결과 값 
            
    
    