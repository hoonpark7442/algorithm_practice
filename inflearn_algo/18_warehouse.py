# 섹션4. 이분탐색(결정알고리즘) & 그리디 알고리즘
# 7. 창고정리

# 내 생각
# 일단.. 정렬하고 리스트의 맨 첫번째값(젤높은거) 하나 빼고 맨 뒤값에 하나 더하고.. 또 한번 정렬..? 이런 식으로 빼고 더하고 정렬..?

# 내 생각 맞나보네

L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
	a[0]+=1
	a[L-1]-=1
	a.sort()

print(a[L-1])-a[0]