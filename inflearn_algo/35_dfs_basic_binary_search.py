# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 2. 이진트리 순회(깊이우선탐색)

# 전위순회
def DFS(v):
	if v > 7:
		return
	else:
		print(v) # 호출 전에 자기 본연의 일을 하면 전위순회
		DFS(v*2)
		DFS(v*2+1)

DFS(1)

# # 중위순회
# def DFS(v):
# 	if v > 7:
# 		return
# 	else:
# 		DFS(v*2)
# 		print(v)
# 		DFS(v*2+1)

# DFS(1)

# # 후위순회
# def DFS(v):
# 	if v > 7:
# 		return
# 	else:
# 		DFS(v*2)
# 		DFS(v*2+1)
# 		print(v)

# DFS(1)