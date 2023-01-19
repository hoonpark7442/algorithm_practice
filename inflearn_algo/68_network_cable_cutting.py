# 섹션8. 동적계획법(Dynamic Programming)
# 2. 네트워크 선 자르기(Top-Down: 재귀, 메모이제이션)

def DFS(len):
	if dy[len]>0:
		return dy[len]
		
	if len==1 or len==2:
		return len
	else:
		dy[len]=DFS(len-1)+DFS(len-2)
		return dy[len]



if __name__="__main__":
	n=int(input())
	dy=[0]*(n+1) # 1부터 사용하려고
	print(DFS(n))