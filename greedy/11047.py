# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:54:21 2022

@author: 오정민
"""

# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.


# 알고리즘 방법
# 해당 돈에 대해서 가장 큰 값부터 차례대로 정렬을 해준 다음에 m 값 보다 크면 pass 작은것부터 각각 더해준다.
# ex 4200 = 1000 + 1000 + 1000 + 1000 + 200
# -> 해당 배열이 1번 사용이 될 떄 마다 count 는 1 씩 증가
# 4200 = 1000 * 4 -> 4번이 사용
# 나머지 부여하여 위와 같은 행위를 반복하여 0이 될때까지 해준다. 
# 4200 = 1000 + 1000 + 1000 + 1000 + 100 + 100 = 6번


n,m = map(int, input().split())

arr=[]
count = 0
target = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

for i in range(n):
    count += m // arr[i]
    m = m % arr[i]

print(count)
    
    

        