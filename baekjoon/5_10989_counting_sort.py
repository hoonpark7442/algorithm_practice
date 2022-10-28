# https://www.acmicpc.net/problem/10989
# 02. 기본정렬 알고리즘 - 핵심유형 문제풀이
# 파이썬 기본 정렬기능으로 못푼다.
# 수의 범위가 제한적일때 계수 정렬(Counting Sort) 사용 -> 시간복잡도 O(N)
# 데이터의 개수가 많을 때 파이썬에서는 input보다 sys.stdin.readline()을 사용해야 한다.

# Counting Sort
# - 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
# - 배열의 크기는 데이터의 범위를 포함할 수 있도록 설정
# - 데이터가 등장한 횟수를 센다.

import sys

n = int(input())
arr = [0] * 10001

for i in range(n):
	data = int(sys.stdin.readline())
	arr[data] += 1

# print("----result----")

for i in range(10001):
	if arr[i] != 0:
		for j in range(arr[i]):
			print(i)



