# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 5. 공주구하기(큐)

# N을 다 큐에 넣음. 하나씩 빼서 뒤에 넣음. 그런데 특정숫자(m)일 때는 안넣음. 뺄때마다 카운팅하고 특정숫자 도달하면 다시 1로 리셋

from collections import deque

n,k=map(int, input().split())
dq=list(range(1, n+1))
dq=deque(dq)
while dq:
	for _ in range(k-1):
		cur=dq.popleft()
		dq.append(cur)
	dq.popleft()
	if len(dq)==1:
		print(dq[0])
		dq.popleft()