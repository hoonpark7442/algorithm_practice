# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 12. 라이브러리를 이용한 순열(9번 수열추측하기를 라이브러리로)

# 라이브러리 이용하는건...그냥 이런게 있다 정도로만 해도 되지 않을까

import itertools as it

n, f = map(int, input().split())
b=[1]*n
cnt=0

for i in range(1, n):
	b[i]=b[i-1]*(n-i)/i

a=list(range(1, n+1))

for tmp in it.permutation(a):
	sum=0
	for L, x in enumerate(tmp):
		sum+=(x*b[L])
	if sum==f:
		for x in tmp:
			print(x, end=' ')
		break

print(cnt)