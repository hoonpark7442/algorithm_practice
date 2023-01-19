# 섹션3. 탐색&시뮬레이션
# 7. 사과나무

# 내 풀이
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# mid = len(arr)//2

# result=0
# idx = 0
# for a in arr[:mid]:
# 	result += sum(a[mid-idx:mid+idx+1])
# 	idx+=1


# idx = 1
# mid_next = mid+1
# for a in arr[mid_next:]:
# 	result += sum(a[idx:n-idx])
# 	idx +=1

# result += sum(arr[mid])

# print(result)

# 문제풀이
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# result = 0
# s=e=n//2

# for i in range(n):
# 	for j in range(s, e+1):
# 		result+=arr[i][j]
# 	if i<n//2:
# 		s-=1
# 		e+=1
# 	else:
# 		s+=1
# 		e-=1

# print(result)





# 2회독차. 내 문제 풀이
# 하..답답하다 정말...

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
sum=0
mid = n//2

for i in range(n):
	if i <= mid:
		b = a[i][mid-i:mid+i+1]
		for j in range(len(b)):
			sum += b[j]
	
	if i > mid:
		c = a[i][i-mid:n-i+mid]
		for j in range(len(c)):
			sum += c[j]

print(sum)













































