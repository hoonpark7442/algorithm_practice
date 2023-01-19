# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 11. 수들의 조합(DFS)

def DFS(L, s, sum):
	global cnt
	if L==k:
		if sum%m==0:
			cnt+=1
	else:
		for i in range(s, n):
			DFS(L+1, i+1, sum+a[i])

n, k = map(int, input().split())
a=list(map(int, input().split()))
m=int(input())
cnt=0
DFS(0,0,0)
print(cnt)