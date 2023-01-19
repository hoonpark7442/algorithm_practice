# https://www.acmicpc.net/problem/1302
# 05. 기본 탐색 알고리즘 - 기초 문제풀이

# 어떻게 풀어야 할까 - 내 생각
# 리스트로 받고, 정렬한 후에, 개수를 세서, 가장 많은 애를 출력

# 내가 푼거
# from collections import Counter

# n = int(input())
# arr = []
# for _ in range(n):
# 	arr.append(input())

# cnt = Counter(sorted(arr))

# print(cnt.most_common(1)[0][0])


# 문제풀이 핵심 아이디어
# - 본 문제는 가장 많이 등장한 문자열을 출력하는 문제와 동일
# - 등장횟수를 계산할 때는 파이썬의 Dictionary 자료형을 이용하면 효과적

# 문제풀이

n = int(input())

books = {}

for _ in range(n):
	book = input()
	if book not in books:
		books[book] = 1
	else:
		books[book] += 1

target = max(books.values())
arr = []

for book, num in books.items():
	if num == target:
		arr.append(book)

print(sorted(arr)[0])