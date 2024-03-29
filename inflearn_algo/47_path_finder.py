# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 15. 경로탐색(그래프 DFS)

# 흠...어케 풀지

# 한 번 방문한 노드는 또 방문하지 않는다.

# def DFS(v):
# 	global cnt
# 	if v == n:
# 		cnt+=1
# 	else:
# 		for i in range(1, n+1):
# 			if g[v][i]==1 and ch[i]==0:
# 				ch[i]=1
# 				DFS(i)
# 				ch[i]=0

# if __name__=="__main__":
# 	n, m = map(int, input().split())
# 	g=[[0]*(n+1) for _ in range(n+1)]
# 	ch=[0]*(n+1)
# 	for i in range(m):
# 		a, b = map(int, input().split())
# 		g[a][b]=1
# 	cnt=0
# 	ch[1]=1
# 	DFS(1)
# 	print(cnt)


# 경로도 다 출력하는 코드

def DFS(v):
	global cnt
	if v == n:
		cnt+=1
		for x in path:
			print(x, end=' ')
		print()
	else:
		for i in range(1, n+1):
			if g[v][i]==1 and ch[i]==0:
				ch[i]=1
				path.append(i)
				DFS(i)
				path.pop()
				ch[i]=0

if __name__=="__main__":
	n, m = map(int, input().split())
	g=[[0]*(n+1) for _ in range(n+1)]
	ch=[0]*(n+1)
	for i in range(m):
		a, b = map(int, input().split())
		g[a][b]=1
	cnt=0
	path=[]
	path.append(1)
	ch[1]=1
	DFS(1)
	print(cnt)









