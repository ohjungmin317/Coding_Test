# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:41:57 2022

@author: 오정민
"""

string = input()

sum = 0

arr =[]

# 문자를 하나씩 확인
for i in string:
    # 숫자인 경우 숫자를 더하기 
    if (ord(i) < 65):
        sum = sum + int(i)
    else: # 숫자가 아닌 경우 알파벳인 경우 그냥 리스트에 대입
        arr.append(i) # i.isalpha()
        
# 알파벳 재정렬        
arr.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if sum !=0:
    arr.append(str(sum))
    
#최종결과 ''를 없이 그냥 출력     
print(''.join(arr))
    