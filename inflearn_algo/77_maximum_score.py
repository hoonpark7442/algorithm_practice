# 섹션8. 동적계획법(Dynamic Programming)
# 11. 최대점수 구하기(냅색 알고리즘)

# 앞에 두 냅색 알고리즘과 다르게 한번만 풀 수 있다. 중복이 안된다. 즉 동전 여러개를 못넣는다.

# 이거 2차원 테이블로 푸셨다...

# dy[i][j] -> i번째, 즉 3이라면 1,2,3번문제까지 적용했을 때라는 뜻. dy[3][15] 이면 3번째 문제까지 푸는데 주어진 시간이 15분

# 한번에 하나만 풀 수 있어서 20분까지의 1분 단위 배열에 문제 5개니까 20*5 배열이 나옴...그래서...참조를...dy[i-1][j-pt] 이렇게...

# 보통 배울땐 2차원으로 설명한다지만 실전에서는 1차원 배열로 풀어야 된다. 문제풀이도 1차원배열로 설명. 문제개수가 100개고 제한시간 1000이면 2차원배열로 하면 답없다.

if __name__=="__main__":
	n, m = map(int, input().split())
	dy=[0]*(m+1)

	for i in range(n):
		ps, pt = map(int, input().split())
		for j in range(m, pt-1, -1):
			dy[j]=max(dy[j], dy[j-pt]+ps)

	print(dy[m])