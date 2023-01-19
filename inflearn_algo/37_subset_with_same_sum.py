# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 4. 합이 같은 부분집합(DFS)
import sys

# def DFS(L, sum): # L은 레벨 혹은 리스트의 인덱스로 봐도 된다.
# 	if L==n:
# 		if sum==(total-sum):
# 			print("YES")
# 			sys.exit(0)
# 	else:
# 		DFS(L+1, sum+a[L])
# 		DFS(L+1, sum)


# n = int(input())
# a=list(map(int, input().split()))
# total = sum(a)
# DFS(0,0)
# print("NO")


# 개선

def DFS(L, sum): # L은 레벨 혹은 리스트의 인덱스로 봐도 된다.
	if sum>total//2:
		return
	if L==n:
		if sum==(total-sum):
			print("YES")
			sys.exit(0)
	else:
		DFS(L+1, sum+a[L])
		DFS(L+1, sum)


n = int(input())
a=list(map(int, input().split()))
total = sum(a)
DFS(0,0)
print("NO")