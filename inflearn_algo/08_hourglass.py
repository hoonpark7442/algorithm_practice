# 섹션3. 탐색&시뮬레이션
# 8. 곳감(모래시계)

# 내 풀이
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# m = int(input())
# cir = [list(map(int, input().split())) for _ in range(m)]

# for a in cir:
# 	m = a[0]-1
# 	arr[m]
# 	new_arr =[0]*n

# 	for j in range(n):
# 		if a[1] == 0:
# 			idx = j-a[2]
# 			if idx < 0:
# 				idx += n	
# 		else:
# 			idx = j+a[2]
# 			if idx >= n:
# 				idx -= n

# 		new_arr[idx] = arr[m][j]

# 	arr[m] = new_arr

# # print(arr)

# s = 0
# e = n
# mid = n//2
# result = 0
# for i in range(n):
# 	for j in range(s, e):
# 		result += arr[i][j]
# 	if i < mid:
# 		s += 1
# 		e -= 1
# 	else:
# 		s -= 1
# 		e += 1

# print(result)

# 문제풀이

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# m = int(input())

# for i in range(m):
# 	h, t, k = map(int, input().split())
# 	if t == 0:
# 		for _ in range(k):
# 			arr[h-1].append(arr[h-1].pop(0))
# 	else:
# 		for _ in range(k):
# 			arr[h-1].insert(0, arr[h-1].pop())

# s = 0
# e = n-1
# mid = n//2
# result = 0
# for i in range(n):
# 	for j in range(s, e+1):
# 		result += arr[i][j]
# 	if i < mid:
# 		s += 1
# 		e -= 1
# 	else:
# 		s -= 1
# 		e += 1

# print(result)









# 2회독차. 내 문제 풀이
# 답지가 더 효율적..

n = int(input())
a= [list(map(int, input().split())) for _ in range(n)]

m=int(input())

for _ in range(m):
	row, direction, num = map(int, input().split())
	temp=[0]*n
	mov = 0
	for i in range(n):
		if direction == 0:
			mov = i-num
			if mov < 0:
				mov = mov+n
		else:
			mov = i+num
			if mov >= n:
				mov = mov-n

		temp[mov] = a[row-1][i]

	a[row-1] = temp

f=0
e=n
mid=n//2
res = 0

for i in range(n):
	for j in range(f,e):
		res += a[i][j]

	if i < mid:
		f+=1
		e-=1
	if i>=mid:
		f-=1
		e+=1

print(res)


















































