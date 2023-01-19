# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 6. 알파코드(DFS)

# 상태트리 어케 그리지...와 모르겠다..

# 문제풀이
# 알파벳 26개 가지를 쭉..

def DFS(L, P):
	global cnt
	if L==n:
		cnt+=1
		for j in range(P):
			print(chr(res[j]+64), end='')
	else:
		for i in range(1,27):
			if code[L]==i:
				res[p]=i
				DFS(L+1, P+1) # P는 인덱스..res용 인덱스...
			elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
				res[P]=i
				DFS(L+2, P+1)


code=list(map(int, input()))
n=len(code)
code.insert(n,-1) # 얘는...code 리스트 맨 마지막 인덱스를 처리할때 두자리수확인하려고 그 뒤 숫자까지 보려하니 에러가 나고..outOfRange 에러 발생
res=[0]*(n+3)
cnt=0
DFS(0, 0)
print(cnt)