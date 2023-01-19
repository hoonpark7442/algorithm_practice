# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 10. 조합 구하기(DFS)

# 중요한 문제. 이 문제 기반으로 많이 응용되어서 나옴
def DFS(L, s):
	global cnt
	if L==m:
		for j in range(L):
			print(res[j], end=' ')
			cnt+=1
			print()
	else:
		for i in range(s, n+1):
			res[L]=i
			DFS(L+1, i+1)


n, m = map(int, input().split())
res=[0]*(n+1)
cnt=0
DFS(0, 1)
print(cnt)
