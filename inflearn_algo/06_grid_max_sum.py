# 섹션3. 탐색&시뮬레이션
# 6. 격자판 최대합

# 내 풀이
# n = int(input())
# arr=[]
# for i in range(n):
# 	arr.append(list(map(int, input().split())))
# arr=[list(map(int, input().split())) for _ in range(n)]

# sum_arr=[]

# for i in range(n):
# 	sum_arr.append(sum(arr[i]))

# for i in range(n):
# 	temp=0
# 	for j in range(n):
# 		temp+=arr[j][i]
# 	sum_arr.append(temp)

# left=0
# for i in range(n):
# 	left += arr[i][i]

# sum_arr.append(left)

# right=0
# r_idx=n
# for i in range(n):
# 	r_idx -= 1
# 	right += arr[i][r_idx]

# sum_arr.append(right)


# print(max(sum_arr))

# 문제풀이(내거랑 거의 비슷한데 더 깔끔)

# n = int(input())
# a=[list(map(int, input().split())) for _ in range(n)]

# largest = -2147000000

# for i in range(n):
# 	sum1=sum2=0
# 	for j in range(n):
# 		sum1+=a[i][j]
# 		sum2+=a[j][i]
# 	if sum1 > largest:
# 		largest=sum1
# 	if sum2 > largest:
# 		largest=sum2

# sum1=sum2=0
# for i in range(n):
# 	sum1+=a[i][i]
# 	sum2+=a[i][n-i-1]

# if sum1 > largest:
# 	largest=sum1
# if sum2 > largest:
# 	largest=sum2


# print(largest)


# 2회독차. 내 문제 풀이
# 2회독째인데.. 어째 뭔가 더 더러워진 느낌...

# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# res = 0

# for i in range(n):
# 	temp = 0
# 	for j in range(n):
# 		temp += a[i][j]

# 	res = max(res, temp)

# temp2 = 0
# for k in range(n):
# 	temp2 += a[k][k]

# temp3 = 0
# for x in range(n):
# 	temp3 += a[n-1-x][n-1-x] # 이부분 틀렸네... 걍 위에 템프2랑 같잖어..


# res_temp = max(temp2, temp3)

# res = max(res, res_temp)

# print(res)






n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
	sum1=sum2=0

	for j in range(n):
		sum1 += a[i][j]
		sum2 += a[j][i]

	if sum1 > largest:
		largest = sum1
	if sum2 > largest:
		largest = sum2

sum1 = sum2 = 0

for i in range(n):
	sum1 += a[i][i]
	sum2 == a[i][n-1-i]

if sum1 > largest:
	largest = sum1
if sum2 > largest:
	largest = sum2


print(largest)




































