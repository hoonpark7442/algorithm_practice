# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 9. 수열 추측하기(순열, 파스칼 응용)

# 이건 너무 수학적인 개념도 많이 들어가고...쉽지 않을거같다... 어렵다

def DFS(L, sum):
	if L==n and sum ==f:
		for x in p:
			print(x, end=' ')
		sys.exit(0)
	else:
		for i in range(1, n+1):
			if ch[i]==0:
				ch[i]=1
				p[L]=i
				DFS(L+1, sum+(p[L]*b[L]))
				ch[i]=0

n,f = map(int, input().split())
p=[0]*n
b=[1]*n
ch=[0]*(n+1)
for i in range(1, n):
	b[i]=b[i-1]*(n-i)//i

DFS(0,0)
