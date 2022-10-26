# https://www.acmicpc.net/problem/1427
# 01. 기본정렬 알고리즘 - 기초문제풀이

arr = input()

for i in range(9,-1,-1):
	for j in arr:
		if int(j) == i:
			print(i, end='')