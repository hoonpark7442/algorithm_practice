# 섹션3. 탐색&시뮬레이션
# 11. 격자판 회문수

# 내 생각
# for 문을 3번만 돈다. 그러고 i에 +5를 해서 i부터 i+5랑 비교해서 같으면 i+1 1+5-1 비교, 이런식으로 회문 검사를 한다. 

board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
	for j in range(7):
		tmp=board[j][i:i+5]
		if tmp==tmp[::-1]:
			cnt+=1
		for k in range(2):
			if board[i+k][j] != board[i+5-k-1][j]:
				break
		else:
			cnt+=1

print(cnt)


# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5
		

















































