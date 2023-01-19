# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 2. 휴가(DFS)

# 어케풀지... 1일째를 한다 안한다로 하고.. 한다고 했을땐...1에 날짜만큼더해서 레벨을 쭉 내리나..? 
# 대충 맞는데 어케 구현할진 몰겠다.

def DFS(L, sum): # L이 날짜
	global res
	if L==n+1:
		if sum>res:
			res=sum
	else:
		if L+T[L]<=n+1:
			DFS(L+T[L], sum+P[L])
		DFS(L+1, sum)


n=int(input())
T=list()
P=list()
for i in range(n):
	a,b = map(int, input().split())
	T.append(a)
	P.append(b)
res=-2147000000
T.insert(0,0) # 0번째 인덱스를 0으로 채우고 나머지는 뒤로 미루기. 즉 인덱스번호를 날짜로 사용
P.insert(0,0)
DFS(1,0)
print(res)