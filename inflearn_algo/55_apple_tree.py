# 섹션7. 깊이/넓이 우선 탐색(DFS, BFS) 활용
# 8. 사과나무(BFS)

# 07번 문제와 같으나 BFS로 풀이


from collections import deque

# 09_mountain에서 쓴 기법
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n= int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
sum=0
Q=deque()
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2, n//2))
L=0

while True:
	if L==n//2:
		break

	size=len(Q)
	for i in range(size):
		tmp=Q.popleft()
		for j in range(4):
			x=tmp[0]+dx[j]
			y=tmp[1]+dy[j]
			if ch[x][y] == 0:
				sum+=a[x][y]
				ch[x][y]=1
				Q.append((x,y))
	L+=1

print(sum)