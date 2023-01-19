# https://www.acmicpc.net/problem/2750
# 01. 기본정렬 알고리즘 - 기초문제풀이

# 1) 선택 정렬 알고리즘

n = int(input())
array = list()

for _ in range(n):
	array.append(int(input()))

for stand in range(n):
	lowest = stand
	for i in range(stand+1,n):
		if array[lowest] > array[i]:
			lowest = i

	array[stand], array[lowest] = array[lowest], array[stand]

for i in array:
	print(i)

# 2) 파이썬 기본 정렬

# n = int(input())
# array = list()

# for _ in range(n):
# 	array.append(int(input()))

# array.sort()

# for i in array:
# 	print(i)