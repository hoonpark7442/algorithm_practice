# 섹션8. 동적계획법(Dynamic Programming)
# 1. 동적계획법이란? 네트워크 선 자르기(Bottom-Up)

# 모르겠다.
# bottom-up -> 작은 단위의 해를 구해서 점점 큰 단위의 해를 구하는 것

n=int(input())
dy=[0]*(n+1) # index0버리고 1부터 사용

dy[1]=1
dy[2]=2

for i in range(3, n+1):
	dy[i]=dy[i-1]+dy[i-2]

print(dy[n])


