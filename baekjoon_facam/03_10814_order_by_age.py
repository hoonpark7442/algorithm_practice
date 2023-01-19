# https://www.acmicpc.net/problem/10814
# 02. 기본정렬 알고리즘 - 핵심유형 문제풀이

n = int(input())

arr = []

for _ in range(n):
	input_data = input().split(' ')
	arr.append((int(input_data[0]), input_data[1]))

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
	print(i[0], i[1])