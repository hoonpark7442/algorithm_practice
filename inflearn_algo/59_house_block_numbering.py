# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 12. 단지번호붙이기(DFS) - BFS로도 풀수있다는데...일단 패스..영상엔 없고 코드만 넣어놨다고 함

# 이건...진심 손도 못대겠다. 

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def DFS(x, y):
	global cnt
	cnt+=1
	board[x][y]=0
	for i in range(4):
		xx=x+dx[i]
		yy=y+dy[i]
		if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
			DFS(xx, yy)

if __name__="__main__":
	n=int(input())
	board=[list(map(int, input())) for _ in range(n)] # split안한이유는 입력값이 띄어쓰기로 안들어와서..
	res=[]
	for i in range(n):
		for j in range(n):
			if board[i][j]==1:
				cnt=0
				DFS(i, j)
				res.append(cnt)

	print(len(res))
	res.sort()
	for x in res:
		print(x)