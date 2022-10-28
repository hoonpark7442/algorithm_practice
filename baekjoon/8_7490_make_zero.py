# https://www.acmicpc.net/problem/7490
# 03. 재귀호출 - 핵심유형 문제풀이

# 문제풀이 핵심 아이디어
# 1. 자연수 N의 범위가 매우 한정적이므로 완전 탐새으로 문제를 해결할 수 있다.
# 2. 수의 리스트와 연산자 리스트를 분리하여 모든 경우의 수를 계산
# 모든 경우의 수 계산은 3^n-1 이다. 수 리스트가 1 2 3 이라 하면 연산자는 저 사이인 두 군데에 들어갈 수 있으므로 연산자 3개 중에 하나 * 연산자 3개 중에 하나 즉 3*3이 된다.
# 1 2 3 4 도 마찬가지이다. 연산자는 저 사이인 세 군데에 들어갈 수 있고, 첫번째칸에 연산자 3개중 하나 * 두번째칸에 연산자3개중하나 * 세번째칸에 연산자3개중하나, 즉 3*3*3이 된다.

# 가능한 모든 경우를 고려하여 연산자 리스트를 만드는 것이 관건(재귀함수이용)

import copy

def recursive(array, n):
	if len(array) == n:
		operators_list.append(copy.deepcopy(array))
		return

	array.append(' ')
	recursive(array, n)
	array.pop()

	array.append('+')
	recursive(array, n)
	array.pop()

	array.append('-')
	recursive(array, n)
	array.pop()

test_case = int(input())

for _ in range(test_case):
	operators_list = []
	n = int(input())
	recursive([], n-1)

	integers = [i for i in range(1, n+1)]

	for operaors in operators_list:
		string = ""
		for i in range(n-1):
			string += str(integers[i]) + operaors[i]
		string += str(integers[-1])
		if eval(string.replace(" ","")) == 0:
			print(string)

	print()
