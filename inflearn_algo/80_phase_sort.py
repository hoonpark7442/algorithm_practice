# 섹션8. 동적계획법(Dynamic Programming)
# 14. 위상정렬(그래프)

# 위상정렬은 일의 선후관계를 유지하며 전체 일의 순서를 짜는 알고리즘

# 방향그래프부터 그려봐라
# 진입차수 리스트도 만들어라

from collections import deque

n,m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()

for i in range(m):
	a,b=map(int, input().split())
	graph[a][b]=1 # 방향그래프니 graph[b][a]는 안해도됨
	degree[b]+=1

for i in range(1, n+1):
	if degree[i]==0:
		dQ.append(i)

while dQ:
	x=dQ.popleft()
	print(x, end=' ')
	for i in range(1, n+1):
		if graph[x][i]==1:
			degree[i]-=1
			if degree[i]==0:
				dQ.append(i)