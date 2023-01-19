# 섹션8. 동적계획법(Dynamic Programming)
# 4. 최대 부분 증가수열(LIS)
# 야 어렵다...

# arr=[5,3,7,8,6,2,9,4]
# 라고 했을 때 앞에서 부터 하나씩 해보는거다. 5가 마지막 항인건 5 하나, 3이 마지막 항인건 3 하나이다. 7이 마지막 항이라 했을 때는? 그 앞에것들 따져보면 되는데, 결국 3 7 혹은 5 7이 된다.
# 8이 마지막 항이라고 했을 때는? 3 7 8, 5 7 8, 3 8, 5 8 이렇게 4가지가 있다. 6은? 3 6, 5 6 이렇게 2개다.

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0) # 1번 인덱스부터 시작하게 하려고
dy=[0]*(n+1)
dy[1]=1
res=0

for i in range(2, n+1):
	max=0
	for j in range(i-1, 0, -1):
		if arr[j]<arr[i] and dy[j]>max:
			max=dy[j]
	dy[i]=max+1
	if dy[i]>res:
		res=dy[i]

print(res)