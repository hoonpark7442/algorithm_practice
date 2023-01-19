# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 14. 안전영역(DFS)

# 이건 더 미쳤네

import sys

sys.setrecursionlimit(10**6) # 흠 재귀 좀 빡세게 돌때 해줘야된다는데 뭔진 잘 모르겠다.

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x,y,h):
	ch[x][y]=1
	for i in range(4):
		xx=x+dx[i]
		yy=y+dy[i]
		if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h:
			DFS(xx,yy,h)

if __name__="__main__":
	n=int(input())
	cnt=0
	res=0
	board=[list(map(int, input().split())) for _ in range(n)]
	for h in range(100):
		ch=[[0]*n for _ in range(n)]
		cnt=0
		for i in range(n):
			for j in range(n):
				if ch[i][j]==0 and board[i][j]>h:
					cnt+=1
					DFS(i,j,h)

		res=max(res, cnt)
		if cnt==0:	# 주어진 행렬에서 최대 높이 까지만 돌면 되고 굳이 99까지 돌릴필요없다. 최대 높이가 뭔지 반복문돌려가며 찾는거보다 이렇게 cnt가0인되는 지점에 도달하면 브레이크걸어주면된다.
			break
	print(res)
