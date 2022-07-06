# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:01:40 2022

@author: 오정민
"""
# p312 곱하기 혹은 더하기
# soultion : + 보다는 x 일 때 값에 대해서 더 큰 수가 된다. 하지만, 0이나 1은 x를 해주는 것 보다는
# +를 해주는 것이 더 값을 증가시켜주기 때문에 1이하의 수에 대해서는 x 보다는 +를 해준다.

data = input()

result = int(data[0]) #입력받은 문자열 데이터를 숫자 데이터로 변환을 해주는 작업

for i in range(1, len(data)):
    
    num = int(data[i])
    
    # 두 수 중에서 하나라도 0이나 1인 경우에는 곱하기 보다는 더하기를 수행해준다.
    if num <=1 or result <=1:
        result = result + num
    # 0이나 1이 아닌 그 외의 수에서는 곱하기를 수행하면 된다.   
    else:
        result = result * num
        
print(result) 
 