# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 13. 섬나라 아일랜드(BFS) 활용

# 흠.....

# 대각선도 포함이라 4방향이 아니라 8방향임
# 단지번호붙이기랑 사실상 같다.

from collections import deque

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]
cnt=0
Q=deque()

for i in range(n):
	for j in range(n):
		if board[i][j]==1:
			board[i][j]=0
			Q.append((i, j))
			while Q:
				tmp=Q.popleft()
				for k in range(8):
					x=tmp[0]+dx[k]
					y=tmp[1]+dy[k]
					if 0<=x<n and 0<=y<n and board[x][y]==1:
						board[x][y]=0
						Q.append((x,y))
			cnt+=1

print(cnt)
