# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 1. 재귀함수르르 이용한 이진수 출력

def DFS(x):
	if x==0:
		return
	else:
		DFS(x//2)
		print(x%2, end='')

n=int(input())
DFS(n)