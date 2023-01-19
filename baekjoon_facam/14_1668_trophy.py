# https://www.acmicpc.net/problem/1668
# 05. 기본 탐색 알고리즘 - 기초 문제풀이

# 어떻게 풀어야 할까 - 내 생각
# 순서대로 돌면서 나보다 큰 수를 카운팅..?

# 내 풀이

# n = int(input())
# arr = []
# left = 0
# right = 0

# for _ in range(n):
# 	arr.append(int(input()))

# l_stand = 0

# for i in arr:
# 	if i > l_stand:
# 		l_stand = i
# 		left += 1

# arr.reverse()

# r_stand = 0

# for i in arr:
# 	if i > r_stand:
# 		r_stand = i
# 		right += 1
# print("--")
# print(left)
# print(right)

# 문제풀이 핵심 아이디어
# - 선반 위에 올려져있는 트로피들에 데해 왼쪽에서, 오른쪽에서 봤을 때 보이는 트로피 수를 각각 구한다.
# - 트로피 개수 N이 최대 50 이므로 단순히 구현하면 된다.

def ascending(arr):
	now = arr[0]
	result = 1
	for i in range(1, len(arr)):
		if now < arr[i]:
			result += 1
			now = arr[i]
	return result

n = int(input())
arr = []

for _ in range(n):
	arr.append(int(input()))

print(ascending(arr))
arr.reverse()
print(ascending(arr))





