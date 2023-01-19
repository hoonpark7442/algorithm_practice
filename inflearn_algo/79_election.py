# 섹션8. 동적계획법(Dynamic Programming)
# 13. 회장뽑기(플로이드-와샬 응용)

# 문제도 어렵다...

if __name__=="__main__":
	n = int(input())
	dis=[[100]*(n+1) for _ in range(n+1)]
	for i in range(1, n+1):
		dis[i][i]=0

	while True:
		a, b = map(int, input().split())
		if a==-1 and b==-1:
			break
		dis[a][b]=1
		dis[b][a]=1 # 무방향 그래프니까 dis[a][b], dis[b][a] 두 개 다 인접행렬 초기화

	for k in range(1, n+1):
		for i in range(1, n+1):
			for j in range(1, n+1):
				dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

	res=[0]*(n+1)
	score=100

	for i in range(1, n+1):
		for j in range(1, n+1):
			res[i]=max(res[i], dis[][j])
		score=min(score, res[i])
	out=[]
	for i in range(1, n+1):
		if res[i]==score:
			out.append(i)

	print("%d %d" %(score, len(out)))
	for x in out:
		print(x, end=' ')