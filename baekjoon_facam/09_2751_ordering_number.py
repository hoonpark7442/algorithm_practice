# https://www.acmicpc.net/problem/2751
# 04. 고급 정렬 알고리즘 - 핵심 유형 문제풀이

# 문제 풀이 핵심 아이디어
# - 데이터 개수가 최대 100만개
# - 최대 시간복잡도 O(NlogN)의 정렬 알고리즘 이용해야 함(왜..?)
# - 고급 정렬 알고리즘(병합, 퀵, 힙)을 이용하여 문제를 해결할 수 있어야 함
# - 혹은 파이썬 기본 정렬 라이브러리 이용하여 문제 풀수도 있음 -> 코테에 나오면 그냥 기본정렬 라이브러리 사용해라

# 퀵 정렬은 O(N^2)까지 나올수도 있어서 제외하고, 이 문제에선 병합정렬을 이용한다.

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	medium = int(len(arr)/2)
	left = merge_sort(arr[:medium])
	right = merge_sort(arr[medium:])

	merged = list()
	l_index, r_index = 0, 0

	while len(left) > l_index and len(right) > r_index:
		if left[l_index] > right[r_index]:
			merged.append(right[r_index])
			r_index += 1
		else:
			merged.append(left[l_index])
			l_index += 1

	while len(left) > l_index:
		merged.append(left[l_index])
		l_index += 1

	while len(right) > r_index:
		merged.append(right[r_index])
		r_index += 1

	return merged


n = int(input())
arr = []

for _ in range(n):
	arr.append(int(input()))

arr = merge_sort(arr)

for data in arr:
	print(data)


# 파이썬 기본 정렬 알고리즘 이용
# n = int(input())
# arr = []

# for _ in range(n):
# 	arr.append(int(input()))

# arr = sorted(arr)

# for data in arr:
# 	print(data)