# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 5. 동전 분배하기(DFS)

# 어려워...어려워....
# 상태트리 그리기가 너무 어려워


def DFS(L): # L은 코인 가짓수..? n이 7 입력되면 7개겠지
	global res
	if L==n:
		diff = max(money)-min(money)
		if diff < res:
			tmp=set()
			for x in money:
				tmp.add(x)
			if len(tmp)==3:
				res=diff

	else:
		for i in range(3):
			money[i]+=coin[L]
			DFS(L+1)
			money[i]-=coin[L]

n=int(input())
coin=[]
money=[0]*3
res=2147000000
for _ in range(n):
	coin.append(int(input()))

DFS(0)
print(res)