# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 10. 최소힙

import heapq as hq

a=[]

while True:
	n=int(input())

	if n == -1:
		break

	if n == 0:
		if len(a) == 0:
			print(-1)
		else:
			print(hq.heappop(a))

	else:
		hq.heappush(a, n)
