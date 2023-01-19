# 섹션8. 동적계획법(Dynamic Programming)
# 12. 플로이드-워셜(그래프 최단거리)

# dis는 2차원 배열. dis[i][j]는 i노드에서 j노드로 가는 최소비용
# 처음 초기화는 직행하는 비용. 즉 인접행렬을 초기화
# 0 6 3 M M
# M 0 M 1 13
# M 2 0 5 M
# M 3 M 0 7
# M M M M 0

# min(dis[i][j], dis[i][k]+dis[k][j])
# i에서 j로 가는 최소비용, i -> k -> j k를 거쳐서 가는 비용

if __name__=="__main__":
	n, m = map(int, input().split())
	dis=[[5000]*(n+1) for _ in range(n+1)]
	for i in range(1, n+1):
		dis[i][i]=0 # 자기에서 자기 자신으로 가는건 다 0으로 초기화

	for i in range(m): # 인접행렬을 만드는 반복문
		a, b, c = map(int, input().split())
		dis[a][b]=c

	for k in range(1, n+1): # 이 삼중포문이 플로이드-워셜 알고리즘
		for i in range(1, n+1):
			for j in range(1, n+1):
				dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])

	for i in range(1, n+1): # 이 부분은 출력 부분
		for j in range(1, n+1):
			if dis[i][j]==5000:
				print("M", end=' ')
			else:
				print(dis[i][j], end=' ')
		print()