# https://www.acmicpc.net/problem/11650
# 02. 기본정렬 알고리즘 - 핵심유형 문제풀이

n = int(input())

arr = []

for _ in range(n):
	x, y = map(int, input().split(' '))
	arr.append((x,y))

arr = sorted(arr)

for i in arr:
	print(i[0], i[1])