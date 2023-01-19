# 섹션6. 완전탐색(백트래킹, 상태트리와 컷엣지) - DFS 기초
# 7. 동전교환(cut edge tech)

# 흠...어케 풀지... 부분집합으로 하려 해도 동전의 종류가 주어진거지 동전의 개수는 무한정인거라 예를 들어 1월짜리 15개로 15원 만들어서 줄수도 있는건데...
# level은 쭉 늘어날수도 있겠는데
# 그리고 동전 큰거붜터 계산해야겠는데.. -> 제일 작은건 너무 레벨이 깊어짐

# 중복순열 문제랑 유사하다함..
# level은 동전을 몇개사용하겠다의 개념이 됨
# 엣지들을 컷 해줘야 한다. res가 1이라고하면 level을 1 아래로 내려갈 필요가 없다든지 등등..

def DFS(L, sum):
	global res
	if L>res:
		return
		
	if sum>m:
		return

	if sum==m:
		if L<res:
			res=L

	else:
		for i in range(n):
			DFS(L+1,sum+a[i])

n=int(input())
a=list(map(int, input().split()))
m=int(input())
res=2147000000
a.sort(reverse=True)
DFS(0,0)


print(res)


