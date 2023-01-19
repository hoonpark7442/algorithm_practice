# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 4. 동전 바꿔주기(DFS)

# 이것도...어렵다...
# 10원 5원 1원짜리 2,3,5개씩
# 흠흠흠 어려워

# 문제풀이
# 허무하네.....


def DFS(L, sum):
	global cnt
	if sum>T:
		return
		
	if L==k:
		if sum==T:
			cnt+=1
	else:
		for i in range(cn[L]+1):
			DFS(L+1, sum+(cv[L]*i))


T=int(input())
k=int(input())
cv=list()
cn=list()
for i in range(k):
	a, b = map(int, input().split())
	cv.append(a)
	cn.append(b)
cnt=0
DFS(0, 0)
print(cnt)