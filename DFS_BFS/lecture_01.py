# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:06:43 2022

@author: 오정민
"""
n, m = map(int, input().split())

graph=[]

# 2차원 리스트 맵 정보 입력 받는 법

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 상 / 하
dy = [0, 0, -1, 1] # 좌 / 우 


# dfs 를 통해 현재 노드를 방문한 뒤 연결된 모든 노드들을 방문
def dfs(x,y):
    
    # 현재 노드는 방문 처리
    graph[x][y] = 1

    # 상 하 좌 우 [ 현재 노드와 인접한 모든 노드들을 탐색하여 방문 가능할 경우 방문]
    for i in range(4):
        
        # 인접한 노드 좌표
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 인접 노드가 내부에 위치하지 않을 때 조건 
        if nx<=1 and nx>=n and ny<=1 and ny>=m:
            return False
        
        # 인접 노드가 내부에 위차하는 조건 
        if(nx>=0 and nx<n and ny>=0 and ny<m):
            
            # 인접 노드에 음료수를 채울 수 있는지 확인
            if(graph[nx][ny] == 0):
                
                # 인접 노드 방문 
                dfs(nx,ny)       
                
# 아이스크림 개수 
result = 0   
             
for i in range(n):
    for j in range(m):
        # 해당 노드에 음료수를 채울 수 있으면 0 이면 채울 수 있음 
        if (graph[i][j]==0):
            # 해당 노드에 대해 dfs 탐색 하여 인접하였는지 확인 
            dfs(i,j)
            result = result + 1


print(result)


# def dfs(x, y):
#     # 2차원 배열에서 벗어나는 경우는 false로 출력 
#     if x<=-1 or x>=n or y<=-1 or y>=m:
#         return False
    
#     if graph[x][y] == 0:
#         graph[x][y] = 1
        
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
        
#         return True
#     return False

# result = 0   
             
# for i in range(n):
#     for j in range(m):
#         if (graph[i][j]==0):
#             dfs(i,j)
#             result = result + 1
    
