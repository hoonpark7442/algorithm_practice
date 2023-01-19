# 섹션8. 동적계획법(Dynamic Programming)
# 9. 가방문제(냅색 알고리즘: Knapsack algorithm)

# dy 리스트부터 만들어봐야 해
# dy[j]: 가방에 j무게 만큼 담을때 보석의 최대 가치
# dy = [0]*최대무게(11키로)

# 먼저 5그램짜리 12가치 갖는 보석 하나만 놓고 보자. dy에서는 일단 5그램이 최대 무게라고 가정하고 시작. 그다음 6그램, 그다음 7그램 이런식으로 늘려가며 가정.


if __name__=="__main__":
	n, m = map(int, input().split())
	dy==[0]*(m+1) # 인덱스번호 0번부터 시작이니까 m까지 생기게 하려면 m+1
	for i in range(n):
		w, v = map(int, input().split())
		for j in range(w, m+1):
			dy[j]=max(dy[j], dy[j-w]+v)

	print(dy[m])

