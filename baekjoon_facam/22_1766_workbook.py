# https://www.acmicpc.net/problem/1766
# 08. 고급 탐색 알고리즘 - 핵심 유형 문제풀이
# 문제유형: 힙, 위상정렬

# 문제풀이 핵심 아이디어
# - 본 문제는 전형적인 위상 정렬 문제 (위상정렬은 힙 자료구조 이용하면 효과적으로 풀 수 있다)
# - 위상 정렬은 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정해주는 알고리즘
# - 위상 정렬 시간복잡도는 O(V+E)

# 위상정렬(Topology Sort) 알고리즘
# 1) 진입 차수가 0인 정점을 큐에 삽입
# 2) 큐에서 원소를 꺼내 해당 원소와 간선을 제거
# 3) 제거 이후에 진입 차수가 0이 된 정점을 큐에 삽입
# 4) 큐가 빌 때 까지 2)-3) 과정 반복

# - 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다는 것임(사이클이 있으면 안됨)
# - 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과

# 역시나 해설은 엉망이다. 위상정렬이 뭔지는 설명했는데 해당 문제에 대해 위상정렬을 어떻게 적용하는지를 설명안한다.

import heapq

n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []

for _ in range(m):
	x, y = map(int, input().split())
	array[x].append(y)
	indegree[y] += 1

for i in range(1, n+1):
	if indegree[i] == 0:
		heapq.heappush(heap, i)

while heap:
	data = heapq.heappop(heap)
	result.append(data)
	for y in array[data]:
		indegree[y] -= 1
		if indegree[y] == 0:
			heapq.heappush(heap, y)

for i in result:
	print(i, end=' ')




import heapq

n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

heap = []
result = []

for _ in range(m):
	x, y = map(int, input().split())
	array[x].append(y)
	indegree[y] += 1

for i in range(1, n+1):
	if indegree[i] == 0:
		heapq.heappush(heap, i)

while heap:
	data = heapq.heappop(heap)
	result.append(data)
	for y in array[data]:
		indegree[y] -= 1
		if indegree[y] == 0:
			heapq.heappush(heap, y)

for i in result:
	print(i, end=' ')





