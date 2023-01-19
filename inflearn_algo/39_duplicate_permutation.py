# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 6. 중복순열구하기

def DFS(L):
	global cnt
	if L==m:
		for j in range(m):
			print(res[j], end=' ')
		print()
		cnt+=1

	else:
		for i in range(1,n+1):
			res[L]=i
			DFS(L+1)

n,m=map(int, input().split())
res=[0]*m
cnt=0
DFS(0)
print(cnt)