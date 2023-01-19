# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 14. 인접행렬(가중치 방향그래프)

# 문제조차 이해 못하겠다...
# 요건 그래프 기본 세팅 하는 법을 위한 강의인거같다. 

n, m = map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
	a, b, c = map(int, input().split())
	g[a][b] = c

for i in range(1, n+1):
	for j in range(1, n+1):
		print(g[i][j], end=' ')
	print()