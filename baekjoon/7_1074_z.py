# https://www.acmicpc.net/problem/1074
# 03. 재귀호출 - 핵심유형 문제풀이

# 강의대로면 안풀리고 저 아래 코드 추가해줘야 풀린다.
def solve(n,x,y):
	global result
	if n == 2:
		if x == X and y == Y:
			print(result)
			return
		result += 1
		if x == X and y+1 == Y:
			print(result)
			return
		result += 1
		if x+1 == X and y == Y:
			print(result)
			return
		result += 1
		if x+1 == X and y+1 == Y:
			print(result)
			return
		result += 1
		return

	# 이부분 추가해 줘야함. 범위내에 없으면 바로 건너뛰기. 근데 왜 소수점붙는지 몰겠다...
	if not (x <= X < x + n and y <= Y < y + n):
		result += n ** 2
		result = int(result)
		return

	solve(n/2, x, y)
	solve(n/2, x, y + n/2)
	solve(n/2, x + n/2, y)
	solve(n/2, x+n/2, y+n/2)

result = 0
N,X,Y = map(int, input().split(' '))
solve(2 ** N, 0, 0)

# https://my-coding-notes.tistory.com/411 참조
# 필요한 곳만 탐색하고 나머지는 빠르게 넘기기 위해 분할 탐색 알고리즘을 사용해야 한다. 
# 분할탐색할 때 중요한 점은 재귀로 모든 부분을 분할하여 탐색하면 안된다는 것이다.
# 그렇게 하면 전체 탐색과 순서만 달라질 뿐이지 결과적으로는 시간복잡도의 개선이 없다.
# 분할탐색은 DP와 반대로 Top-Down 방식이다.
# 코드는 https://codingcocoon.tistory.com/151 여기 참조

# import sys

# result = 0

# def solve(n, x, y):
#     global result
#     if x == r and y == c:
#         print(int(result))
#         exit(0)

#     if n == 1:
#         result += 1
#         return

#     # 원하는 좌표가 범위내에 있지 않으면 result에 한번에 값 처리해서 넣고 리턴한다.
#     if not (x <= r < x + n and y <= c < y + n):
#         result += n * n
#         return
#     solve(n / 2, x, y)
#     solve(n / 2, x, y + n / 2)
#     solve(n / 2, x + n / 2, y)
#     solve(n / 2, x + n / 2, y + n / 2)


# n, r, c = map(int, sys.stdin.readline().split(' '))
# solve(2 ** n, 0, 0)
