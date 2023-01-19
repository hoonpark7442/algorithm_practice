# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 7. 송아지 찾기(BFS)

# BFS는 레벨 탐색
# 큐를 사용
# 레벨이 거리를 뜻하는 거니 최단거리 문제를 푸는데에 BFS가 좋다?

from collections import deque

MAX=10000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
n,m = map(int, input().split())
ch[n]=1
dis[n]=0
dq=deque()
dq.append(n)

while dq:
	now=dq.popleft()
	if now==m:
		break

	for next in(now-1, now+1, now+5):
		if 0<next<=MAX:
			if ch[next]==0:
				dq.append(next)
				ch[next]=1
				dis[next]=dis[now]+1

print(dis[m])