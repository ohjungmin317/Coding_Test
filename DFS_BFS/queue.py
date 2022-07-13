# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:53:08 2022

@author: 오정민
"""

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(5)
queue.append(6)
queue.append(7)
queue.append(8)
queue.popleft()
queue.popleft()


print(queue)
queue.reverse()
print(queue)