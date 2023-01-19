# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 1. 최대점수 구하기(DFS)

# N만큼 뻗기.. 5분 12분 8분 3분 4분 뻗고... 5분에선 자신 제외한 나머지 4개로 뻗고... 뻗을 때 마다 sum값이 20인지 체크. 만약 20 넘으면 종료. 딱 20일 땐 그 sum값을 일단 저장. 
# 저장시 최대인지 확인하고 값 더 작으면 갱신안함.

# 아니네.... 상태트리가 다르네ㅜㅜ 

def DFS(L, sum, time):
	global res
	if time>m:
		return

	if L==n:
		if sum>res:
			res=sum
	else:
		DFS(L+1, sum+pv[L], time+pt[L]) # 문제 풀기로 선택한거
		DFS(L+1, sum, time) # 문제 안풀기로 선택한거



n, m = map(int, input().split())
pv=list()
pt=list()

for i in range(n):
	a, b = map(int, input().split())
	pv.append(a)
	pt.append(b)

res = -2147000000
DFS(0,0,0)
print(res)