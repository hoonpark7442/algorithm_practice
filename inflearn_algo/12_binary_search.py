# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 1. 이분 검색

n, m = map(int, input().split())
a=list(map(int, input().split()))

a.sort()
lt=0
rt=n-1
while lt <= rt:
	mid = (lt+rt)//2
	if a[mid]==m:
		print(mid+1)
		break
	elif a[mid]>m:
		rt=mid-1
	else:
		lt=mid+1