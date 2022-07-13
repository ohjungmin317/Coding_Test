# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:50:08 2022

@author: 오정민
"""

stack=[]

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.pop()
stack.append(5)
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()

print(stack) # 먼저 넣은 순서대로
print(stack[::-1]) # 나중에 넣은 순서대로 