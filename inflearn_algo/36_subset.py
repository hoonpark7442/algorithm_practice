# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 3. 부분집합구하기(DFS)

# DFS 잘하려면 상태트리 잘 구성하면 된다. 
# 상태트리는 상태를 전이하는 건데 해당 강의 4분 30초 쯤 봐라.

def DFS(v):
	if v == n+1:
		for i in range(1, n+1):
			if ch[i]==1:
				print(i, end=' ')
		print()
	else:
		ch[v]=1
		DFS(v+1)
		ch[v]=0
		DFS(v+1)


n = int(input())
ch=[0]*(n+1)
DFS(1)