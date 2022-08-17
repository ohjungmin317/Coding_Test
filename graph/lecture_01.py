# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:26:39 2022

@author: 오정민
"""
# p298
# 학교에서 학생들에게 0번부터 N번까지의 번호를 부여했다. 처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N + 1 개의 팀이 존재한다. 이때 선생님은 '팀 합치기'연산과 '같은 팀 여부 확인'연산을 사용할 수 있다.

# '팀 합치기' 연산은 두 팀을 합치는 연산이다.
# '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
# 선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다. (1 <= N, M <= 100,000)
# 다음 M개의 줄에는 각각의 연산이 주어진다.
# '팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
# '같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
# a와 b는 N 이하의 양의 정수이다.
# '같은 팀 여부 확인'연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.


def find_team(team, x): # 개선된 서로소 집합 알고리즘 (경로 압축 기법)
    if team[x] != x:
        team[x] = find_team(team, team[x])
    return team[x]

def union_team(team,a,b): # union 합치는 기능을 해주는 함수 
    a = find_team(team, a)
    b = find_team(team, b)
    
    if a < b:
        team[b] = a
    else:
        team[a] = b 

n,m = map(int, input().split())
team = [0] * (n+1) # 초기화 (부모 테이블)

for i in range(1, n+1):
    team[i] = i # 부모 자기 자신으로 초기화 

for i in range(m):
    n,a,b = map(int, input().split()) # 입력을 받는 곳 
                                        # 0 a b ->  a번 속한 팀과 b번 학생이 속한 팀을 합치는 의미
                                        # 1 a b ->  a번 학생과 b번 학생이 같은 팀에 속해 있는지 확인하는 연산 ( 사이클 여부 확인 하는 알고리즘 ) 
    
    if n == 0:
        union_team(team, a, b)
    
    elif n == 1:
        if find_team(team, a) == find_team(team, b): # 사이클 여부 확인하는 하는 알고리즘 
            print('YES')
        else:
            print('NO')
    