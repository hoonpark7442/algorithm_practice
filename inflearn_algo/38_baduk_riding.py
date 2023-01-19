# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 5. 바둑이승차(cut edge tech)

# 부분집합이랑 같은 문제임
# 원소 1개짜리 부분집합, 2개짜리 부분집합, ... 이렇게 부분집합 만드는거임

def DFS(L, sum, tsum):
	global result
	if sum+(total-tsum)<result:
		return

	if sum>c:
		return

	if L == n:
		if sum>result:
			result=sum
	else:
		DFS(L+1, sum+a[L], tsum+a[L])
		DFS(L+1, sum, tsum+a[L])

c, n = map(int, input().split())
a=[0]*n
result=-2147000000
for i in range(n):
	a[i] = int(input())
total=sum(a)
DFS(0, 0, 0)
print(result)
