# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 17. 피자배달거리(DFS)

# 모르겠어 역시나
# 이게 (예제기준) 6콤비네이션4 의 문제라고..?
# 어렵다어려워 설명들어도 모르겠다.

def DFS(L, s):
	global res
	if L==m:
		sum=0 # 도시 피자거리
		for j in range(len(hs)):
			x1=hs[j][0]
			y1=hs[j][1]
			dis=2147000000
			for x in cb:
				x2=pz[x][0]
				y2=pz[x][1]
				dis=min(dis, abs(x1-x2)+abs(y1-y2))
			sum+=dis
		if sum<res:
			res=sum

	else:
		for i in range(s, len(pz)):
			cb[L]=i
			DFS(L+1, i+1)



if __name__="__main__":
	n, m = map(int, input().split())
	board=[list(map(int, input().split())) for _ in range(n)]
	hs=[]
	pz=[]
	cb=[0]*m # combination
	res=2147000000
	for i in range(n):
		for j in range(n):
			if board[i][j]==1:
				hs.append((i,j))
			elif board[i][j]==2:
				pz.append((i,j))
	DFS(0,0)