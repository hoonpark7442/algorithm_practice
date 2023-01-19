# 섹션8. 동적계획법(Dynamic Programming)
# 10. 동전교환(냅색알고리즘)

# dy[j]: j원을 거슬러주는데 사용된 동전의 최소 개수
# dy는 최소값 찾는거기때문에 초기화를 큰 수로 해야함. 500원이 최대라니까 500개로 하진 말고 넉넉히 1000개로 초기화

if __name__=="__main__":
	n=int(input())
	coin=list(map(int, input().split()))
	m=int(input())
	dy=[1000]*(m+1)
	dy[0]=0

	for i in range(n):
		for j in range(coin[i], m+1):
			dy[j]=min(dy[j], dy[j-coin[i]]+1)

	print(dy[m])
