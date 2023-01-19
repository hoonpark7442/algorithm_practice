# https://www.acmicpc.net/problem/1939
# 06. 기본 탐색 알고리즘 - 핵심유형 문제풀이
# 문제유형: 이진탐색 문제

# 어렵다...

# 문제 풀이 핵심 아이디어
# - 다리 개수 M은 최대 10만이며 중량제한 C는 최대 10억개. 즉 로그를 씌우던가 하는 이진탐색 생각을 해봐야 한다.
# - 이진 탐색을 이용하여 O(M*logC)에 문제를 해결할 수 있다.
# - 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최대값을 이진 탐색으로 찾는다.
# - BFS를 사용해야 한다... 
# - BFS는 간선의 개수만큼의 시간복잡도가 걸린다. 즉 O(M). 여기에 중량에 대해 로그씌워서 logC 만큼 곱한게 시간복잡도가 된다. 약 3백만 
# - 해당 강의의 18분 정도부터 보면서 이해해야 한다.

# case1
# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3

# 추가 케이스
# 3 3
# 1 2 9
# 3 1 2
# 2 3 5
# 1 3

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)] # 인덱스 0부터 하려면 복잡해지니 그냥 1부터 하려고 range(n+1)로 함

def bfs(c):
	queue = deque([start_node]) # queue가 need_visit queue
	visited = [False] * (n+1)
	visited[start_node] = True

	while queue:
		x = queue.popleft() # x가 node
		for y, weight in adj[x]:
			if not visited[y] and weight >= c:
				visited[y] = True
				queue.append(y)
	return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
	x, y, weight = map(int, input().split())
	adj[x].append((y, weight))
	adj[y].append((x, weight))
	start = min(start, weight)
	end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while(start <= end):
	mid = (start+end) // 2 # mid는 현재의 중량을 의미
	if bfs(mid): # 이동이 가능하므로 중량을 증가시킴
		result = mid
		start = mid + 1
	else:	# 이동이 불가능하므로 중량을 감소시킴
		end = mid - 1

print(result)


# from collections import deque

# n, m = map(int, input().split())
# adj = [[] for _ in range(n+1)]

# def bfs(c):
# 	queue = deque([start_node])
# 	visited = [False] * (n+1)
# 	visited[start_node] = True

# 	while queue:
# 		x = queue.popleft()
# 		for y, weight in adj[x]:
# 			if not visited[y] and weight >= c:
# 				visited[y] = True
# 				queue.append(y)
# 	return visited[end_node]

# start = 1000000000
# end = 1

# for _ in range(m):
# 	x, y, weight = map(int, input().split())
# 	adj[x].append((y, weight))
# 	adj[y].append((x, weight))
# 	start = min(weight, start)
# 	end = max(weight, end)

# start_node, end_node = map(int, input().split())

# result = start
# while(start <= end):
# 	mid = (start+end)//2
# 	if bfs(mid):
# 		result = mid
# 		start = mid+1
# 	else:
# 		end = mid - 1

# print(result)





