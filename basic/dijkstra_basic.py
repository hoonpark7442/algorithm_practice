import heapq

mygraph = {
	'A':{'B':8,'C':1,'D':2},
	'B':{},
	'C':{'B':5,'D':2},
	'D':{'E':3,'F':5},
	'E':{'F':1},
	'F':{'A':5}
}

def dijkstra(graph, start):
	# 초기화 스타트
	distances = {node:float('inf') for node in graph}
	distances[start] = 0
	queue = []

	heapq.heappush(queue, [distances[start], start])
	# 초기화 엔드

	while queue:
		current_distance, current_node = heapq.heappop(queue)

		if distances[current_node] < current_distance:
			continue

		for adjacent, weight in graph[current_node].items():
			disance = current_distance + weight

			if disance < distances[adjacent]:
				distances[adjacent] = disance
				heapq.heappush(queue, [disance, adjacent])

	return distances

temp = dijkstra(mygraph, 'A')

print(temp)