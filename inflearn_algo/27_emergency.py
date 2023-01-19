# 섹션5. 자료구조 활용(스택,큐,해쉬,힙)
# 6. 응급실(큐)

# 음...인덱스를 트래킹해야되나? 큐 안에 있는 애들 크기는 어떻게 비교를 하지..? 생각보다 까다롭네...
# 강의에선 어렵지 않다고 말하네..
# 내림차순 정렬은 안된다. 이건 나도 그렇게 생각.

from collections import deque

n,m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0

while True:
	cur=Q.popleft()
	if any(cur[1]<x[1] for x in Q):
		Q.append(cur)
	else:
		cnt+=1
		if cur[0]==m:
			break

print(cnt)
