# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 8. 순열구하기(DFS)

# 어렵..

def DFS(L):
	global cnt
	if L==m:
		for j in range(L):
			print(res[j], end=' ')
		print()
		cnt+=1
	else:
		for i in range(1, n+1):
			if ch[i]==0:
				ch[i]=1
				res[L]=i
				DFS(L+1)
				ch[i]=0


n, m = map(int, input().split())
res=[0]*n
ch=[0]*(n+1)
cnt=0
DFS(0)
print(cnt)
